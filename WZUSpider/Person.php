<?php
/**
 * Created by PhpStorm.
 * User: Julis
 * Date: 2018/6/9
 * Time: 下午12:56
 */

class Person
{
    private $name;
    private $id;
    private $test_id;
    private $sex;
    private $leave;
    private $idetify_id;
    private $class;
    private $college;
    private $image;

    /**
     * @return mixed
     */
    public function getImage()
    {
        return $this->image;
    }

    /**
     * @param mixed $image
     */
    public function setImage($image)
    {
        $this->image = $image;
    }

    /**
     * @return mixed
     */
    public function getTestId()
    {
        return $this->test_id;
    }

    /**
     * @param mixed $test_id
     */
    public function setTestId($test_id)
    {
        $this->test_id = $test_id;
    }

    /**
     * @return mixed
     */
    public function getSex()
    {
        return $this->sex;
    }

    /**
     * @param mixed $sex
     */
    public function setSex($sex)
    {
        $this->sex = $sex;
    }

    /**
     * @return mixed
     */
    public function getLeave()
    {
        return $this->leave;
    }

    /**
     * @param mixed $leave
     */
    public function setLeave($leave)
    {
        $this->leave = $leave;
    }

    /**
     * @return mixed
     */
    public function getIdetifyId()
    {
        return $this->idetify_id;
    }

    /**
     * @param mixed $idetify_id
     */
    public function setIdetifyId($idetify_id)
    {
        $this->idetify_id = $idetify_id;
    }

    /**
     * @return mixed
     */
    public function getClass()
    {
        return $this->class;
    }

    /**
     * @param mixed $class
     */
    public function setClass($class)
    {
        $this->class = $class;
    }

    /**
     * @return mixed
     */
    public function getCollege()
    {
        return $this->college;
    }

    /**
     * @param mixed $college
     */
    public function setCollege($college)
    {
        $this->college = $college;
    }



    /**
     * @return mixed
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * @param mixed $name
     */
    public function setName($name)
    {
        $this->name = $name;
    }

    /**
     * @return mixed
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * @param mixed $id
     */
    public function setId($id)
    {
        $this->id = $id;
    }
    public function __toString()
    {
        // TODO: Implement __toString() method.

        return ',温州大学,'.$this->getTestId().','.
            $this->getName().','.$this->getId().','.$this->getSex().','.
            $this->getIdetifyId().','.$this->getCollege().','.
            $this->getClass().','.$this->getLeave().','.
            $this->getImage().'<br>';
    }

}