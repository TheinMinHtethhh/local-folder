import java.util.*;
public class InstanceTest{
	

    public  static void main( String[]  ags ) { 
	Scanner sc = new Scanner(System.in);
	Convert1 cvt = new Convert1();

	System.out.println("あんたの身長をインチで教えてください。");
	int userHeightInInches = sc.nextInt();
	int heightToCm = cvt.inchTocm(userHeightInInches);
	System .out. println( userHeightInInches +"インチ　は約"+heightToCm+"cm" +" です" ) ;

	System.out.println("変換したいポンドを教えてください。");
	double userWeightInKg= sc.nextDouble();
	double userPoundToKg = cvt.poundTokg(userWeightInKg);
	System.out.println(userWeightInKg +"ポンド　は約　"+userPoundToKg+"kg");

	System.out.println("変換したい華氏温度を教えてください。");
	int userTinF = sc.nextInt();
	int FerToCel = cvt.FtoC(userTinF);
	System.out.println( userTinF +" 華氏温度は約　"+ FerToCel + "°C"+ "です");

	
	System.out.println("僕の身長は　"+ Convert1.height*1.2 + " です");
    }
}
class Convert1{
    int inchTocm(double a){
	return(int)(2.54*a);
} 
  
    double poundTokg(double w){
	return (0.454*w);
}
   int FtoC(int d){
	return(int)((5.0/9.0)*(d-32));
}
    public static double height = 167.0;
}

