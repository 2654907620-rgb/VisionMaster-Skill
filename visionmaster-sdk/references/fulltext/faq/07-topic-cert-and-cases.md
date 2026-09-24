# 专题：认证教程 + VM应用案例
<!-- pages 801-995 -->

<!-- page 801 -->
HIKROBOT 
 
792 
 
 
这一步是重头戏，算子封装的绝大部分工作量就在这一步：  
不过幸运的是，开发者并不需要从头到尾了解一遍工程的源代码结构，源码的各个部分的
作用，集成算子的开发者只需要关注一个Process 函数即可，封装算子的代码其实就是将
Process 具体的实现一遍。  
 
开发者需要获取的输入就在modu_input 中，比如我们要获取定制模块的订阅的图像源的
图像，将此图像原始字节数据转成Halcon 可以处理的HImage 格式，实现的代码如下所
示：  
 
我们从modu_input 拿到了Halcon 可以处理的图像HObject 类型的HImage, 那接着
用Halcon 算子处理算法流就可以了。比如使用Halcon 的动态阈值，典型的代码如下所
示：  



<!-- page 802 -->
HIKROBOT 
 
793 
 
 
 
第三步：如何获取模块的输入。自动生成的C++工程已经帮我们生成好了类库的成员变
量，例如，以本例来说，定义的输入就是成员变量：  
 
我们在Process 中可以直接使用，当用户界面设置了某个参数，比如说最小过滤面积，通
过参数配置界面设置成了1000，那么当模块执行的时候，m_nMinArea 的值就会是100
0。无需开发者写代码从界面去拿，这一切都是自动的。  
当然这其中并没有什么高深复杂的内部机制，实际上，获取输入参数和设置输出参数，都
是靠VM 代理模块在后台去执行GetParam 和SetParam 做到的。GetParam 和SetPara
m 的代码清楚的显示了，它是如何做到这一点的。  
这里摘取其中的代码片段，如下：  
获取输入参数  



<!-- page 803 -->
HIKROBOT 
 
794 
 
 
 
设置运行参数  
 
第四步：如何设置模块的输出  
设置算法工具的输出主要靠下面几个接口函数：  
 



<!-- page 804 -->
HIKROBOT 
 
795 
 
 
 
 
 
我们举例说明，例如我有一个结果输出，输出的是Blob 结果中最大的那个团块的面积，
我们就需要用到VM_M_SetFloat 这个接口函数，示例代码如下：  
 
示例代码中“MaxArea”等，就是模块的XML 文件中描述的算法模块的输出名称，也是
这个模块的结果输出Tab 页中显示的结果名称。  
如果要一次性设置多个输出，可以使用VM_M_BatchSetXXX(XXX 代指数据类型) 
 
 
 
让我们举例说明，例如我有一个结果输出，输出的是Blob 得到的最小外接矩形结果，显
然这个结果是包含多种结果的，我们就需要用到VM_M_BatchSetFloat 这个接口函数，
示例代码如下  



<!-- page 805 -->
HIKROBOT 
 
796 
 
 
 
示例代码中“BlobResultRectX”等，就是模块的XML 文件中描述的算法模块的输出名
称，也是这个模块的结果输出Tab 页中显示的结果名称。  
3 调试方法  
将生成好的算法模块DLL 拷贝到DynThreshold 文件夹中，再将DynThreshold 文件夹
拷贝到VM 的Applications\Module(sp)\x64 目录下的模块类别下。我们运行VisionMa
ster 软件，在VM 软件中加载用户自定义的模块之后，可以在VS 中附加进程，这个进程
是“VmModuleProxy”,附加了进程后就可以设置断点调试了。  
如下图所示：  
 



<!-- page 806 -->
HIKROBOT 
 
797 
 
 
接着选择VmModuleProxy 进程  
 
如果发现调试时，发现不能命中断点，一定是没有将算法模块DLL 对于的调试信息pdb
文件拷贝到Module(sp)目录下的工具组目录下的算法模块目录。拷贝过去就可以命中断
点了。  
4 写在最后  
在VM 中集成第三个的算法工具，展示的是VM 的开放性，VM 可以集成第三方的算法，
用来增强和扩展VM 的能力集，这是VM 一个比较好的特性。但开发者一定要注意，第三
方的算法会涉及到版权和授权的问题，这个需要开发者遵循相关的版权协议及相应的法律
条款，与VisionMaster 算法平台无关。  



<!-- page 807 -->
HIKROBOT 
 
798 
 
 
问题根因  
1. 不了解VisionMaster 可以集成第三方算子模块  
2. 不知道从哪里入手来封装第三方算子  
3. 对XML 界面生成器不了解  
4. 对C++封装算子的编程不够了解，特别是如何将第三方图像格式转换成VM 能处
理的图像格式不清楚。  
 
 



<!-- page 808 -->
HIKROBOT 
 
799 
 
 
4.4 异常处理 
4.4.1 环境配置：运行算子模块Demo 时，
无法找到v120 的生成工具 
描述  
环境：VM4.0 及以上 + VS2017 
现象：运行算子模块Demo 时，报错提示无法找到v120 的生成工具。 
解答  
此现象是由于算子模块自动的生成的代码的环境是VS2013，所以此时可以通过两种方式
来解决：第一种则是通过下载VS2013 来获取v120 的生成工具；第二种则是直接升级的
生成工具（推荐）。  
第二种方式的具体步骤：  
1、右击项目名称，选择属性，打开项目的属性页，将平台工具集改成当前VS2017 版本
对应的v141。  



<!-- page 809 -->
HIKROBOT 
 
800 
 
 
 
2、右击项目名称，选择重定向项目，选择相应的SDK 版本。  
 
问题根因  
不熟悉如何升级VS 工具集。  
 
 
 
 



<!-- page 810 -->
HIKROBOT 
 
801 
 
 
专题 
1 认证教程 
1.1 VM4.2 中级教程_VM SDK 开发 
 
 
 



<!-- page 811 -->
HIKROBOT 
 
802 
 
 
 
 



<!-- page 812 -->
HIKROBOT 
 
803 
 
 
 
 



<!-- page 813 -->
HIKROBOT 
 
804 
 
 
 
 



<!-- page 814 -->
HIKROBOT 
 
805 
 
 
 
 



<!-- page 815 -->
HIKROBOT 
 
806 
 
 
 
 



<!-- page 816 -->
HIKROBOT 
 
807 
 
 
 
 



<!-- page 817 -->
HIKROBOT 
 
808 
 
 
 
 



<!-- page 818 -->
HIKROBOT 
 
809 
 
 
 
 



<!-- page 819 -->
HIKROBOT 
 
810 
 
 
 
 



<!-- page 820 -->
HIKROBOT 
 
811 
 
 
 
 



<!-- page 821 -->
HIKROBOT 
 
812 
 
 
 
 



<!-- page 822 -->
HIKROBOT 
 
813 
 
 
 
 



<!-- page 823 -->
HIKROBOT 
 
814 
 
 
 
 



<!-- page 824 -->
HIKROBOT 
 
815 
 
 
 
 



<!-- page 825 -->
HIKROBOT 
 
816 
 
 
 
 



<!-- page 826 -->
HIKROBOT 
 
817 
 
 
 
 



<!-- page 827 -->
HIKROBOT 
 
818 
 
 
 
 



<!-- page 828 -->
HIKROBOT 
 
819 
 
 
 
 



<!-- page 829 -->
HIKROBOT 
 
820 
 
 
 
 



<!-- page 830 -->
HIKROBOT 
 
821 
 
 
 
 



<!-- page 831 -->
HIKROBOT 
 
822 
 
 
 
 



<!-- page 832 -->
HIKROBOT 
 
823 
 
 
 
 



<!-- page 833 -->
HIKROBOT 
 
824 
 
 
 
 



<!-- page 834 -->
HIKROBOT 
 
825 
 
 
 
 



<!-- page 835 -->
HIKROBOT 
 
826 
 
 
 
 



<!-- page 836 -->
HIKROBOT 
 
827 
 
 
 
 



<!-- page 837 -->
HIKROBOT 
 
828 
 
 
 
 
 
 



<!-- page 838 -->
HIKROBOT 
 
829 
 
 
1.2 VM4.x 中级教程_算子 SDK 开发 
 
 
 



<!-- page 839 -->
HIKROBOT 
 
830 
 
 
 
 



<!-- page 840 -->
HIKROBOT 
 
831 
 
 
 
 



<!-- page 841 -->
HIKROBOT 
 
832 
 
 
 
 



<!-- page 842 -->
HIKROBOT 
 
833 
 
 
 
 



<!-- page 843 -->
HIKROBOT 
 
834 
 
 
 
 



<!-- page 844 -->
HIKROBOT 
 
835 
 
 
 
 



<!-- page 845 -->
HIKROBOT 
 
836 
 
 
 
 



<!-- page 846 -->
HIKROBOT 
 
837 
 
 
 
 



<!-- page 847 -->
HIKROBOT 
 
838 
 
 
 
 



<!-- page 848 -->
HIKROBOT 
 
839 
 
 
 
 



<!-- page 849 -->
HIKROBOT 
 
840 
 
 
 
 



<!-- page 850 -->
HIKROBOT 
 
841 
 
 
 
 



<!-- page 851 -->
HIKROBOT 
 
842 
 
 
 
 



<!-- page 852 -->
HIKROBOT 
 
843 
 
 
 
 



<!-- page 853 -->
HIKROBOT 
 
844 
 
 
 
 



<!-- page 854 -->
HIKROBOT 
 
845 
 
 
 
 



<!-- page 855 -->
HIKROBOT 
 
846 
 
 
 
 



<!-- page 856 -->
HIKROBOT 
 
847 
 
 
 
 



<!-- page 857 -->
HIKROBOT 
 
848 
 
 
 
 
 
 
 



<!-- page 858 -->
HIKROBOT 
 
849 
 
 
1.3 VM4.2 中级教程_算法模块开发 
 
 



<!-- page 859 -->
HIKROBOT 
 
850 
 
 
 
 



<!-- page 860 -->
HIKROBOT 
 
851 
 
 
 
 



<!-- page 861 -->
HIKROBOT 
 
852 
 
 
 
 



<!-- page 862 -->
HIKROBOT 
 
853 
 
 
 
 



<!-- page 863 -->
HIKROBOT 
 
854 
 
 
 
 



<!-- page 864 -->
HIKROBOT 
 
855 
 
 
 
 



<!-- page 865 -->
HIKROBOT 
 
856 
 
 
 
 



<!-- page 866 -->
HIKROBOT 
 
857 
 
 
 
 



<!-- page 867 -->
HIKROBOT 
 
858 
 
 
 
 



<!-- page 868 -->
HIKROBOT 
 
859 
 
 
 
 



<!-- page 869 -->
HIKROBOT 
 
860 
 
 
 
 



<!-- page 870 -->
HIKROBOT 
 
861 
 
 
 
 



<!-- page 871 -->
HIKROBOT 
 
862 
 
 
 
 



<!-- page 872 -->
HIKROBOT 
 
863 
 
 
 
 



<!-- page 873 -->
HIKROBOT 
 
864 
 
 
 
 



<!-- page 874 -->
HIKROBOT 
 
865 
 
 
 
 



<!-- page 875 -->
HIKROBOT 
 
866 
 
 
 
 



<!-- page 876 -->
HIKROBOT 
 
867 
 
 
 
 
 



<!-- page 877 -->
HIKROBOT 
 
868 
 
 
1.4 VM4.x 中级教程_标定与定位技术 
 
 
 



<!-- page 878 -->
HIKROBOT 
 
869 
 
 
 
 



<!-- page 879 -->
HIKROBOT 
 
870 
 
 
 
 



<!-- page 880 -->
HIKROBOT 
 
871 
 
 
 
 



<!-- page 881 -->
HIKROBOT 
 
872 
 
 
 
 



<!-- page 882 -->
HIKROBOT 
 
873 
 
 
 
 



<!-- page 883 -->
HIKROBOT 
 
874 
 
 
 
 



<!-- page 884 -->
HIKROBOT 
 
875 
 
 
 
 



<!-- page 885 -->
HIKROBOT 
 
876 
 
 
 
 



<!-- page 886 -->
HIKROBOT 
 
877 
 
 
 
 



<!-- page 887 -->
HIKROBOT 
 
878 
 
 
 
 



<!-- page 888 -->
HIKROBOT 
 
879 
 
 
 
 



<!-- page 889 -->
HIKROBOT 
 
880 
 
 
 
 



<!-- page 890 -->
HIKROBOT 
 
881 
 
 
 
 



<!-- page 891 -->
HIKROBOT 
 
882 
 
 
 
 



<!-- page 892 -->
HIKROBOT 
 
883 
 
 
 
 



<!-- page 893 -->
HIKROBOT 
 
884 
 
 
 
 



<!-- page 894 -->
HIKROBOT 
 
885 
 
 
 
 



<!-- page 895 -->
HIKROBOT 
 
886 
 
 
 
 



<!-- page 896 -->
HIKROBOT 
 
887 
 
 
 
 
 



<!-- page 897 -->
HIKROBOT 
 
888 
 
 
1.5 VM4.3 中级教程_VM SDK 开发 
 
 



<!-- page 898 -->
HIKROBOT 
 
889 
 
 
 
 



<!-- page 899 -->
HIKROBOT 
 
890 
 
 
 
 



<!-- page 900 -->
HIKROBOT 
 
891 
 
 
 
 



<!-- page 901 -->
HIKROBOT 
 
892 
 
 
 
 



<!-- page 902 -->
HIKROBOT 
 
893 
 
 
 
 



<!-- page 903 -->
HIKROBOT 
 
894 
 
 
 
 



<!-- page 904 -->
HIKROBOT 
 
895 
 
 
 
 



<!-- page 905 -->
HIKROBOT 
 
896 
 
 
 
 



<!-- page 906 -->
HIKROBOT 
 
897 
 
 
 
 



<!-- page 907 -->
HIKROBOT 
 
898 
 
 
 
 



<!-- page 908 -->
HIKROBOT 
 
899 
 
 
 
 



<!-- page 909 -->
HIKROBOT 
 
900 
 
 
 
 



<!-- page 910 -->
HIKROBOT 
 
901 
 
 
 
 



<!-- page 911 -->
HIKROBOT 
 
902 
 
 
 
 



<!-- page 912 -->
HIKROBOT 
 
903 
 
 
 
 



<!-- page 913 -->
HIKROBOT 
 
904 
 
 
 
 



<!-- page 914 -->
HIKROBOT 
 
905 
 
 
 
 



<!-- page 915 -->
HIKROBOT 
 
906 
 
 
 
 



<!-- page 916 -->
HIKROBOT 
 
907 
 
 
 
 



<!-- page 917 -->
HIKROBOT 
 
908 
 
 
 
 



<!-- page 918 -->
HIKROBOT 
 
909 
 
 
 
 



<!-- page 919 -->
HIKROBOT 
 
910 
 
 
 
 



<!-- page 920 -->
HIKROBOT 
 
911 
 
 
 
 



<!-- page 921 -->
HIKROBOT 
 
912 
 
 
 
 



<!-- page 922 -->
HIKROBOT 
 
913 
 
 
 
 



<!-- page 923 -->
HIKROBOT 
 
914 
 
 
 
 
 
 
 



<!-- page 924 -->
HIKROBOT 
 
915 
 
 
1.6 VM4.3 中级教程_算法模块开发 
 
 



<!-- page 925 -->
HIKROBOT 
 
916 
 
 
 
 



<!-- page 926 -->
HIKROBOT 
 
917 
 
 
 
 



<!-- page 927 -->
HIKROBOT 
 
918 
 
 
 
 



<!-- page 928 -->
HIKROBOT 
 
919 
 
 
 
 



<!-- page 929 -->
HIKROBOT 
 
920 
 
 
 
 



<!-- page 930 -->
HIKROBOT 
 
921 
 
 
 
 



<!-- page 931 -->
HIKROBOT 
 
922 
 
 
 
 



<!-- page 932 -->
HIKROBOT 
 
923 
 
 
 
 



<!-- page 933 -->
HIKROBOT 
 
924 
 
 
 
 



<!-- page 934 -->
HIKROBOT 
 
925 
 
 
 
 



<!-- page 935 -->
HIKROBOT 
 
926 
 
 
 
 



<!-- page 936 -->
HIKROBOT 
 
927 
 
 
 
 



<!-- page 937 -->
HIKROBOT 
 
928 
 
 
 
 



<!-- page 938 -->
HIKROBOT 
 
929 
 
 
 
 



<!-- page 939 -->
HIKROBOT 
 
930 
 
 
 
 



<!-- page 940 -->
HIKROBOT 
 
931 
 
 
 
 



<!-- page 941 -->
HIKROBOT 
 
932 
 
 
 
 



<!-- page 942 -->
HIKROBOT 
 
933 
 
 
 
 



<!-- page 943 -->
HIKROBOT 
 
934 
 
 
 
 



<!-- page 944 -->
HIKROBOT 
 
935 
 
 
 
 



<!-- page 945 -->
HIKROBOT 
 
936 
 
 
 
 
 
 



<!-- page 946 -->
HIKROBOT 
 
937 
 
 
2.1 VM 应用案例 
 
 



<!-- page 947 -->
HIKROBOT 
 
938 
 
 
2.2.1 外观检测：利用VM 实现缺陷检测及
尺寸量测  
描述  
环境：VM4.0.0  
现象：如何使用VM 进行检测与测量？  
解答  
1 功能需求  
某客户现场要对生产的PCB 板进行多项检测，主要对三个区域进行检测分别为：区域1，
检测锡片的有无。区域1，检测锡片的外观完整性。区域2，测量装配件的长度d1 (图像
中为上下端的高度)、测量区域3 圆心到区域2 装配件上端的距离d2。每次拍照后，视觉
软件将总检测状态(OK 为1，NG 为0)、以及两个测量值(物理值)发给上位机。如下图所
示。  



<!-- page 948 -->
HIKROBOT 
 
939 
 
 
 
2 检测步骤  
首先分析需求，该项目主要分为检测与测量两个部分。其中，检测分为有无检测以及外观
完整性检测，可以通过检测区域1 的亮度来判断有无，通过检测区域1 较亮区域的面积判
断外观是否完整；测量在这里分为两个部分，分别为线与线之间距离的测量，圆心点与线
之间距离的测量。这个项目完整的流程编辑如下图所示。  



<!-- page 949 -->
HIKROBOT 
 
940 
 
 
 
第一步：首先增加图像源模块，双击图像源模块，按照实际情况配置图像源（本地图像、
相机、SDK），实际生产中通常使用相机，本地调试一般选择本地图像，通过SDK 接口给
图则选择SDK。注意在使用相机之前需要在快捷工具栏中的全局相机配置相机。  



<!-- page 950 -->
HIKROBOT 
 
941 
 
 
 
第二步：增加高精度匹配模块，使用连线连接，双击高精度匹配模块，配置参数，首先
设。置图像源，通常为图像源模块的输出图像。  



<!-- page 951 -->
HIKROBOT 
 
942 
 
 
 
之后，点击特征模板中的创建，使用掩膜工具，选择合适的特征区域，设定合适的配置，
参数创建合适的模板。需要注意的是，配置参数通常使用默认参数的自动模式，如果无法
满足需求，可以切换手动模式进行调节，其中速度尺度与特征尺度控制模板的精细程度，
影响模板匹配的速度，特征尺度越大，精细程度越低，匹配速度越快；调节对比度阈值影
响可以建立想要建立的模板。  



<!-- page 952 -->
HIKROBOT 
 
943 
 
 
 
 



<!-- page 953 -->
HIKROBOT 
 
944 
 
 
建立好模板之后，需要设置运行参数，包括最小匹配分数，匹配个数，匹配极性，角度范
围尺度范围等。最小匹配参数设置越高，匹配越严格；匹配个数代表允许查找的匹配，当
有多个匹配时，默认匹配分数最高的项；匹配极性代表建立的模板与背景之间的过渡亮暗
是否一致；角度范围指建立的模板与可能存在的匹配项之间可以允许的角度变化，改参数
会影响匹配的速度，角度范围设置越大，匹配速度越慢。  
如果调节上述参数无法满足使用的要求，可以调节运行参数中的高级参数，其中最大重叠
率代表匹配多个目标时，可以允许的目标之间的重叠情况；延拓阈值一般在匹配目标位于
图像边缘，匹配不全时使用。  



<!-- page 954 -->
HIKROBOT 
 
945 
 
 
 



<!-- page 955 -->
HIKROBOT 
 
946 
 
 
第三步：增加位置修正模块，使用连线连接，双击模块，参数一般选择默认参数，点击一
次执行，点击创建基准。  
 
第四步：增加亮度检测模块，使用连线连接，双击模块，设置如图所示的ROI。  



<!-- page 956 -->
HIKROBOT 
 
947 
 
 
 
第五步：增加Blob 分析模块，使用连线连接，双击模块，设置如图所示的ROI。  



<!-- page 957 -->
HIKROBOT 
 
948 
 
 
 
之后，根据实际项目情况设置运行参数。  



<!-- page 958 -->
HIKROBOT 
 
949 
 
 
 
第六步：增加条件检测模块，使用连线连接，双击模块，订阅希望进行判断的参数，并且
设置有效值范围。  



<!-- page 959 -->
HIKROBOT 
 
950 
 
 
 
到这里，本次项目的检测部分已经全部完成，下面进行测量部分。  
第七步：增加直线查找模块，使用连线连接，双击模块，根据要查找的直线设置ROI。  



<!-- page 960 -->
HIKROBOT 
 
951 
 
 
 
之后，设置运行参数，其中边缘类型表示想要查找的直线的特征；边缘极性表示按照搜寻
方向灰度值的变化情况；边缘阈值表示梯度阈值；滤波尺寸表示想要的边缘的抗噪能力，



<!-- page 961 -->
HIKROBOT 
 
952 
 
 
该数值越大，则抗噪能力越强，但同时也可能导致真正的边缘被滤除；卡尺数量表示查找
直线需要使用卡尺工具找出的点的数量；剔除点数表示拟合时被排除的最小点的数量，该
参数需要结合剔除距离共同设置；  
如果上述的运行参数无法满足项目需要，可以设置高级参数。剔除距离表示允许的离群点
到查找的直线的最大像素距离；投影宽度表示扫描边缘点查找ROI 的区域宽度；初始拟合
表示进行直线拟合的方式，一般选择全局拟合；拟合方式表示进行直线拟合的算法选择。  
 



<!-- page 962 -->
HIKROBOT 
 
953 
 
 
第七步：增加直线查找模块与圆查找模块，使用连线连接，参照上述直线查找的过程查找
圆。  
第八步：增加格式化模块，使用连线连接，双击配置想要输出的内容。  
 
格式化结果如下所示，注意这里输出的是像素距离，实际中需要乘以当像素代表的实际物
理尺寸。  



<!-- page 963 -->
HIKROBOT 
 
954 
 
 
 
第九步：增加发送数据模块，使用连线连接，选择通信方式，这里以TCP 通信，并且默认
视觉软甲是服务端，选择通信设备。需要注意的是，TCP 服务端需要在快捷栏中的通信管
理中进行配置。  



<!-- page 964 -->
HIKROBOT 
 
955 
 
 
 
这样，我们就完成了这个本项目所有的检测与测量的需求，并且可以对下位机发送通信信
号。之后，打开网络通信助手验证，是否可以正常通信。网络通信助手输出结果如下所
示。  



<!-- page 965 -->
HIKROBOT 
 
956 
 
 
 
问题根因  
不熟悉VM 做项目的流程。  
 
 



<!-- page 966 -->
HIKROBOT 
 
957 
 
 
2.2.2 图像检索：使用VM 深度学习功能实
现模型训练与图像检索功能  
描述  
环境：VM4.0.0 及以上  
现象：如何使用VM 深度学习工具自己训练模型实现图像检索功能。  
解答  
1.图像检索原理  
图像检索主要分为图像的表示学习和分类器注册两部分。图像的表示学习就是通过构建网
络模型实现图像的特征表示，分类器注册就是将表示学习网络输出的图像特征向量输入分
类器进行分类器注册。使用VM 实现图像检索前也需要进行模型训练和分类器注册。  
图像检索和图像分类的区别：图像分类是直接训练一个固定类别数的分类器模型；图像检
索是训练一个图像表示模型，然后针对不同的检索库注册不同的分类器模型，从而避免了
针对不同检索库需要训练不同网络模型的麻烦，提升网络模型的泛化能力。  
2.基于VM 的图像检索方法  
2.1 打标签  



<!-- page 967 -->
HIKROBOT 
 
958 
 
 
可以使用VMTrain1.4.0 来进行数据集打标签工作，添加图片是对单张图片进行打标，添
加文件夹是对多张图片批量打标签。打标签的结果如图所显示。  
 
2.2 模型训练  
模型训练有三种环境可以选择：本地训练(需要支持深度学习加速的NVIDIA 显卡和CUDA
环境)、云服务器训练和本地服务器训练。训练参数:训练迭代次数(可以根据数据量来调
整)、基础学习率(可以控制模型的收敛速度)、版本、剪枝比例(模型压缩手段，可以根据模
型性能和精度来权衡调整)、数据增强(数据集扩充手段，用于丰富数据量，防止过拟合)。
参数设置完毕，点击开始训练。训练结束在指定为文件夹下会生成bin 文件(模型权重文
件)。  
2.3 注册图像  



<!-- page 968 -->
HIKROBOT 
 
959 
 
 
在VM 中使用DL 图像检索模块中的Gallery 管理中的注册图像按钮进行图像注册，可以
单张图像注册，也可以按文件夹注册(可以针对不同的检索库注册不同的Gallery,执行时按
需要加载gall 文件)。  
 
2.4 图像检索  
图像检索方案如图所示，主要使用DL 图像检索模块进行图像检索。  
 



<!-- page 969 -->
HIKROBOT 
 
960 
 
 
参数配置：需要加载训练好的模型文件(VisionTrain 训练得到的bin 文件)和注册好的Gall
ery 文件(gall 文件)。  
 
2.5 检索结果  



<!-- page 970 -->
HIKROBOT 
 
961 
 
 
 
问题根因  
不熟悉VM 深度学习训练工具的使用。  
 
 



<!-- page 971 -->
HIKROBOT 
 
962 
 
 
2.2.3 字符识别：使用VM 进行字符识别 
描述  
环境：VM4.0.0  
现象：如何使用VM 进行字符识别？  
解答  
1 功能需求：对如下图所示的铭牌上的字符进行识别，并将识别出的字符发送给上位机。
  
 
2 检测步骤：首先分析需求，该项目的主要需求为字符识别，可以使用字符识别模块完成
识别，为了便于字符识别过程中进行图像分割，从而训练字符，首先需要对该图像的检测
区域进行预处理。这个项目完整的流程编辑如下图所示。  



<!-- page 972 -->
HIKROBOT 
 
963 
 
 
 
第一步：首先增加图像源模块，双击图像源模块，选择本地图像。  



<!-- page 973 -->
HIKROBOT 
 
964 
 
 
 
第二步：使用高精度匹配模块和位置修正模块进行粗定位。增加高精度匹配模块，使用连
线连接，双击高精度匹配模块，配置参数，首先设置图像源，通常为图像源模块的输出图
像。之后，点击特征模板中的创建，使用掩膜工具，选择合适的特征区域，设定合适的配
置，参数创建合适的模板。本案例中，创建的模板如下所示：  



<!-- page 974 -->
HIKROBOT 
 
965 
 
 
 
建立好模板之后，根据具体项目情况设置合理的运行参数，在这里设置最小匹配分数为0.
5，最大匹配个数为1，匹配极性设置为考虑极性，角度范围根据物料可能旋转角度的实际
情况设置，这里设置为-20 到20 尺度范围，尺度范围设置为0.98 到1.02，高级参数使用
默认参数。  



<!-- page 975 -->
HIKROBOT 
 
966 
 
 
 
增加位置修正模块，使用连线连接，双击模块，参数选择默认参数，点击一次执行，再点
击创建基准。  
第三步：为了便于进行字符分割从而训练字符，需要对图像做一些预处理工作。首先添加
图像二值化模块，选择图像源作为输入源，并绘制ROI，运行参数选择自动二值化。  
二值化结果如下图所示：  



<!-- page 976 -->
HIKROBOT 
 
967 
 
 
 
 
第四步：可以看到二值化后的图像仍然存在着干扰，不利于字符的分割与训练，可以使用
形态学处理模块来去除干扰。增加形态学处理模块，使用连线连接，双击模块，选择图像
源作为输入源，并绘制ROI，设置运行参数，其中开运算与腐蚀用来断开图像边界之间的



<!-- page 977 -->
HIKROBOT 
 
968 
 
 
粘连，闭运算与膨胀用来闭合图像边界之间的间隙。形态学形状指结构元素的形状，运算
结果图像轮廓会和形态学形状比较相似。  
 
形态学处理的结果如下图所示：  
 



<!-- page 978 -->
HIKROBOT 
 
969 
 
 
第五步：可以看见图像的干扰被去除，下面使用字符识别模块进行训练与识别，增加字符
识别模块，使用连线连接，双击模块，选择形态学处理的输出图像作为输入源，并绘制R
OI。在运行参数界面点击字符训练，  
 
框选待识别的字符区域，设置相关参数，其中，距离阈值指字符片段到文本基线的距
离，大于该值则无法被提取；字符间隙指两个字符间的最小横向间距；点击提取字
符，字符区域将被分割成一个个单独的被红色框框住的字符区域。  



<!-- page 979 -->
HIKROBOT 
 
970 
 
 
 
点击训练字符，将被分割字符区域代表的字符填入字符框，点击添加至字符库。这样就完
成了字符库的训练。  



<!-- page 980 -->
HIKROBOT 
 
971 
 
 
 
在运行参数中，根据实际情况，决定是否需要开启字符过滤，这里以开启字符过滤为例，
点击字符过滤，启用字符过滤，设置相关参数，其中，识别字符个数代表需要进行字符识
别的字符数量，字符类型用来设置需要识别的每个字符的类型。  



<!-- page 981 -->
HIKROBOT 
 
972 
 
 
 
设置运行参数中的相关参数，其中，有白底黑字和黑底白字两种；字符宽度范围与字符高
度范围的参数范围是[1,512]，需要根据待识别的字符的宽度与高度进行设置；宽度类型有
可变类型和等宽类型两种类型。当字符宽度一致时选择等宽类型，当字符宽度有差异选择
可变类型；片段面积代表单个字符所能允许像素面积范围；合格阈值指能够被识别字符的
最小得分。  



<!-- page 982 -->
HIKROBOT 
 
973 
 
 
 
根据实际情况，决定是否需要进行高级参数的设置，其中，距离阈值指字符片段到文本基
线的距离，大于该值则会被删除；忽略边框指是否忽略与ROI 粘连的字符；主方向范围代
表文本行倾斜角度搜索范围；倾斜角范围指允许字符倾斜的最大范围；最大宽高比代表单
个字符外接矩形的最大宽高比，取值范围是；字符滤波使能指是否开启字符间字符宽度的
滤波使能；笔画宽度范围代表单个笔画的宽度范围，在打开宽度滤波使能后才能生效。  



<!-- page 983 -->
HIKROBOT 
 
974 
 
 
 
字符识别的结果如下图所示：  
 
第九步：增加发送数据模块，使用连线连接，选择通信方式，这里以TCP 通信，并且默认
视觉软件是服务端，选择通信设备。需要注意的是，TCP 服务端需要在快捷栏中的通信管
理中进行配置。  



<!-- page 984 -->
HIKROBOT 
 
975 
 
 
 
这样，我们就完成了字符识别，并且可以对下位机发送识别字符。  
问题根因  
不熟悉VM 字符识别模块的使用。  
 
 



<!-- page 985 -->
HIKROBOT 
 
976 
 
 
2.2.4 联合开发：VM 脚本联合OpenCV 开
发  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：VM 脚本联合OpenCV 开发  
解答  
首先需要进行OpenCV 环境的配置  
第一步：双击打开脚本模块  
 



<!-- page 986 -->
HIKROBOT 
 
977 
 
 
第二步：点击“编辑程序集 ”按钮 
 
第三步：点击添加按钮，将VM 安装路径下三方库中的OpenCV 动态库，全部选中并添
加到引用中 
 



<!-- page 987 -->
HIKROBOT 
 
978 
 
 
 
点击打开后，会报出如下错误  
 
这是因为OpenCV 库中的OpenCvSharpExtern.dll 引用失败，需要手动拷贝到脚本依赖
目录下  
第四步：将OpenCvSharpExtern.dll 拷贝到VM 脚本模块依赖目录下 



<!-- page 988 -->
HIKROBOT 
 
979 
 
 
 
第五步：在脚本中添加OpenCV 的命名空间  
 



<!-- page 989 -->
HIKROBOT 
 
980 
 
 
上述操作即可完成OpenCV 在VM 脚本中配置，可以在脚本中直接调用OpenCVSharp
中的相关函数API 进行图像处理。  
其次，需要在脚本中实现ImageData 图像类型和OpenCVSharp 中Mat 类型
的转换  
第一步：设置输入变量与输出变量，类型均为IMAGE 类型  
 
第二步：引用System.Runtime.InteropServices 命名空间  



<!-- page 990 -->
HIKROBOT 
 
981 
 
 
 
第三步：将输入的imagedata 类型转换成Mat 类型，设置相应的ROI 并调用OpenCV
库中的接口，进行图像渲染后，将Mat 类型转换成imagedata 类型，进行输出。 
1. C#  
2. //实例化ImageData 类型图像 
3. ImageData img = new ImageData(); 
4. GetImageValue("in0", ref img); 
5. ImageData imgOut = new ImageData(); 
6. Mat srcImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV
_8UC1); 
7.   
8. Rect rect = new Rect(0, 0, 300, 300); 
9.   



<!-- page 991 -->
HIKROBOT 
 
982 
 
 
10. if (img.PixelFormat == ImagePixelFormate.MONO8) 
11. { 
12.      //开辟内存空间 
13.      IntPtr grayPtr = Marshal.AllocHGlobal(img.Width * img.He
igth); 
14.      //向内存空间中写入数据 
15.      Marshal.Copy(img.Buffer, 0, grayPtr, img.Buffer.Length); 
16.   
17.      //imagedata 转Mat 
18.      srcImage = new Mat(img.Heigth, img.Width, MatType.CV_
8UC1, grayPtr);    
19.      //设置ROI             
20.      Mat imageROI = new Mat(srcImage, rect); 
21.      Mat dstImage = Mat.Zeros(imageROI.Height, imageROI.Wi
dth, MatType.CV_8UC1); 
22.      //调用OpenCV 中的接口进行图像处理 
23.      Cv2.Threshold(imageROI,dstImage,10,120,ThresholdTypes.O
tsu); 
24.      //将处理后的图像拷贝到原图ROI 区域 
25.      dstImage.CopyTo(imageROI); 



<!-- page 992 -->
HIKROBOT 
 
983 
 
 
26.      byte[] datab = new Byte[srcImage.Width * srcImage.Heig
ht]; 
27.   
28.      //mat 转ImageData 
29.      srcImage.GetArray(0, 0, datab); 
30.      imgOut.Buffer = datab; 
31.      imgOut.Width = srcImage.Width; 
32.      imgOut.Heigth = srcImage.Height; 
33.      imgOut.PixelFormat = ImagePixelFormate.MONO8; 
34.   
35.      //用完记得释放指针 
36.      Marshal.FreeHGlobal(grayPtr); 
37. } 
38. SetImageValue("imageOut", imgOut); 
问题根因  
不熟悉VM 脚本联合OpenCV 开发的方法。  
提示  
鼠标选中脚本模块，按Ctrl+M 快捷键，可以直接跳转到脚本模块目录。  



<!-- page 993 -->
HIKROBOT 
 
984 
 
 
 
 



<!-- page 994 -->
HIKROBOT 
 
985 
 
 
2.2.5 联合开发：VM 脚本联合OpenCV 实
现轮廓查找  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何利用VM 脚本联合OpenCV 实现轮廓查找与绘制。 
解答  
1. 采集灰度图，如下图所示  
 
2. 脚本中获取海康图像内存对象数据  
1. ImageData img = new ImageData(); 



<!-- page 995 -->
HIKROBOT 
 
986 
 
 
2. GetImageValue("in0", ref img); 
3. 将海康图像格式ImageData 转换为OpenCV Mat 图像格式  
1. Mat srcImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV
_8UC1);       
2. Mat dstImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV
_8UC1); 
3. if (img.PixelFormat == ImagePixelFormate.MONO8) 
4. { 
5.  //开辟内存空间 
6.  IntPtr grayPtr = Marshal.AllocHGlobal(img.Width * img.Heigt
h); 
7.  //向内存空间中写入数据      
8.  Marshal.Copy(img.Buffer, 0, grayPtr, img.Buffer.Length); 
9.  //ImageData 转 Mat  
10.  srcImage = new Mat(img.Heigth, img.Width, MatType.CV_8U
C1, grayPtr); 
11. } 
4. 依次进行Canny 边缘检测、轮廓查找  
1. //调用OpenCV 中函数接口进行图像处理 


