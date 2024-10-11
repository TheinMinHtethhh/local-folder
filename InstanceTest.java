import java.util.*;
public class InstanceTest{
	

    public  static void main( String[]  ags ) { 
	Scanner sc = new Scanner(System.in);
	Convert1 cvt = new Convert1();
       	int a = cvt.inchTocm(3.5);
	System .out. println( "3.5インチは約 "+a+"cm"  ) ;

	double b = cvt.poundTokg(9);
	System.out.println("9ポンドは約　"+b+"kg");

	int c = cvt.FtoC(100);
	System.out.println("100°F は　"+ c + "°C");
    }
}
class Convert1{
    int inchTocm(double a){
	return(int)(2.54*a);
} 
  
    double poundTokg(int w){
	return (0.454*w);
}
   int FtoC(int d){
	return(int)((5.0/9.0)*(d-32));
}
}

