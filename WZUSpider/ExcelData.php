<?php

/**
 * Created by PhpStorm.
 * User: Julis
 * Date: 2018/6/8
 * Time: 下午9:52
 */


require_once 'PHPExcel-1.8/Classes/PHPExcel.php';
require_once 'PHPExcel-1.8/Classes/PHPExcel/Writer/Excel2007.php';
require_once 'PHPExcel-1.8/Classes/PHPExcel/Writer/Excel5.php';
require_once 'PHPExcel-1.8/Classes/PHPExcel/IOFactory.php';
//error_reporting(-1);
//ini_set('display_errors', 1);
class ExcelData{


    public function get_excel_data($file_name){
        //读取
        $file=$file_name;
        if(!file_exists($file)){
            die("要操作的文件不存在！");
        }
        //取文档的类型（与扩展名无关）
        $filetype=PHPExcel_IOFactory::identify($file);
        //创建 一个特定的读取类
        $excelread=PHPExcel_IOFactory::createReader($filetype);
        //加载文件
        $phpexcel=$excelread->load($file);
        //读取一个工作表，可以通过索引或名称
        $sheet=$phpexcel->getSheet(0);
        //获取当前工作表的行数
        $rows=$sheet->getHighestRow();
        //获取当前工作表的列（在这里获取到的是字母列），
        $column=$sheet->getHighestColumn();
        //把字母列转换成数字，这里获取的是列的数，并且列的索引
        $columns=PHPExcel_Cell::columnIndexFromString($column);

        $arr=[];
        //创建一个表头数组，个数与列数一致
        $title=array("name","id");
        //通过循环把表格中读取到的数据，存入二维数据，以便后期数据库的写入操作，行是从1开始的
        for ($i=2;$i<=$rows;$i++){
            $arr_col=[];
            //列是从0开始的
            for ($col=0;$col<$columns;$col++){
                //把数字列转换成字母列，这里是通的列索引获取到对应的字母列
                $columnname=PHPExcel_Cell::stringFromColumnIndex($col);
                $arr_col[$title[$col]]=$sheet->getCell($columnname.$i)->getValue();
            }
            $arr[]=$arr_col;
        }

        return $arr;
    }
    public function getExcel($fileName,$headArr,$data){
        if(empty($data) || !is_array($data)){
            die("data must be a array");
        }
        if(empty($fileName)){
            exit;
        }
        $date = date("Y_m_d",time());
        $fileName .= "_{$date}.xlsx";

        //创建新的PHPExcel对象
        $objPHPExcel = new PHPExcel();
        $objProps = $objPHPExcel->getProperties();

        //设置表头
        $key = ord("A");
        foreach($headArr as $v){
            $colum = chr($key);
            $objPHPExcel->setActiveSheetIndex(0) ->setCellValue($colum.'1', $v);
            $key += 1;
        }

        $column = 2;
        $objActSheet = $objPHPExcel->getActiveSheet();
        foreach($data as $key => $rows){ //行写入
            $span = ord("A");
            foreach($rows as $keyName=>$value){// 列写入
                $j = chr($span);
                $objActSheet->setCellValue($j.$column, $value);
                $span++;
            }
            $column++;
        }

        $fileName = iconv("utf-8", "gb2312", $fileName);
        //重命名表
        $objPHPExcel->getActiveSheet()->setTitle('Simple');
        //设置活动单指数到第一个表,所以Excel打开这是第一个表
        $objPHPExcel->setActiveSheetIndex(0);
        //将输出重定向到一个客户端web浏览器(Excel2007)
        header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
        header("Content-Disposition: attachment; filename=\"$fileName\"");
        header('Cache-Control: max-age=0');
        $objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel2007');
//        if(!empty($_GET['excel'])){
            $objWriter->save('php://output'); //文件通过浏览器下载
//        }else{
//            $objWriter->save($fileName); //脚本方式运行，保存在当前目录
//        }
        exit;

    }
}
