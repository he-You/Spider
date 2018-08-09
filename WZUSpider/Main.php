<?php
/**
 * Created by PhpStorm.
 * User: Julis
 * Date: 2018/6/9
 * Time: 下午12:53
 */
require_once 'ExcelData.php';
require_once 'Person.php';


//error_reporting(-1);
//ini_set('display_errors', 1);

$starttime = explode(' ',microtime());
excute();
//$arr[]=array();
//$time=0;
//
//foreach($persons as $person){
//    $arr[$time++]=array(
//        $person->getName(),
//        $person->getID(),
//        $person->getSex(),
//        $person->getCollege(),
//        $person->getClass(),
//        $person->getLeave(),
//        $person->getIdetifyId(),
//        $person->getTestId(),
//        $person->getImage()
//       );
//
//}


//$fileName = "export_test";
//$headArr = array("姓名","学号","性别","学院","班级","等级","身份证号","考号","照片");
//
//$data = array($arr);
//$excel=new ExcelData();
//$excel->getExcel($fileName,$headArr,$data);
//
$endtime = explode(' ',microtime());
$thistime = $endtime[0]+$endtime[1]-($starttime[0]+$starttime[1]);
$thistime = round($thistime,3);
echo '总共用时:'.$thistime.'秒';



/**
 * 执行
 */
function excute(){
    $excel=new ExcelData();
    $file_name='number.xls';
    $excel_data=$excel->get_excel_data($file_name);
    $time=0;
    $arr[]=array();
    foreach ($excel_data as $person_array){
        $starttime = explode(' ',microtime());
        curl_get($person_array['name'],$person_array['id'], $time++);

//        if($person){
//            $arr[$time++]=$person;
//        }

        $endtime = explode(' ',microtime());
        $thistime = $endtime[0]+$endtime[1]-($starttime[0]+$starttime[1]);
        $thistime = round($thistime,3);
        echo ",".$thistime;
    }
    echo "共：".$time;


}

/**
 * 获取网页资源
 * @param $name
 * @param $id
 * @return Person
 */
function curl_get($name,$id,$time){
    $url='http://jwc.wzu.edu.cn/yy46dy.jsp?urltype=tree.TreeTempUrl&wbtreeid=1121&condition1='.base64_encode('{xh='.$id.', xm='.$name.'}');

    $ch=curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch,CURLOPT_HEADER,1);
    $result=curl_exec($ch);
    $code=curl_getinfo($ch,CURLINFO_HTTP_CODE);
    if($code!='404' && $result){
        return  get_more_person_info($result,$name,$id,$time);
    }
    curl_close($ch);
}

/**
 * 获取数据资源
 * @param $content
 * @param $name
 * @param $s_id
 * @return int|Person
 */
function get_more_person_info($content,$name,$s_id,$time){
    $level_testid_pattern='/<td><span class="textspan">(.*?)<\/span><\/td>/';
    preg_match_all($level_testid_pattern, $content, $matches);
    $level=$matches[1][0];
    if(empty($level)){
        return 0;
    }
    $test_id=$matches[1][1];
    $id_college_class_pattern='/<td colspan="3"><span class="textspan2">(.*?)<\/span><\/td>/';
    preg_match_all($id_college_class_pattern, $content, $matches);
    $sex=substr($matches[1][0],-3);
    $id=$matches[1][1];
    $college=$matches[1][2];
    $class=$matches[1][3];
    $image_pattern='/<img id=\'imgUser\' height="93px" width="70px" src="(.*?)"/';
    preg_match_all($image_pattern, $content, $matches);
    $image="http://jwc.wzu.edu.cn/".$matches[1][0];
    $person=new Person();
    $person->setName($name);
    $person->setId($s_id);
    $person->setClass($class);
    $person->setIdetifyId($id);
    $person->setSex($sex);
    $person->setTestId($test_id);
    $person->setCollege($college);
    $person->setLeave($level);
    $person->setImage($image);

//    echo $time.$person;
}