
public class Shbsearch {

	/**
	 * @param args
	 */
	public int search(int n,int[] a){
		int rstnum=0;
		int len=a.length;
		for(int i=0;i<len-1;i++)
			if(a[i]>a[i+1])
				rstnum=i+1;
		System.out.println(rstnum);
		int l=0;
		int r=len-1;
		int m;
		int tmp;
		int res=-1;
		while(l<=r){
			m=(l+r)/2;
			if(m>(len-1-rstnum))
				tmp=m-(len-rstnum);
			else
				tmp=m+rstnum;
			//System.out.println(tmp);
			if(a[tmp]<n)
				l=m+1;
			else if(a[tmp]>n)
				r=m-1;
			else{
				res=tmp;
				return res;
			}

		}
		return res;
	}
	public static void main(String[] args) {
		Test t=new Test();
		int [] a={6,7,1,2,3,4,4};
		int res=t.search(3, a);
		System.out.println(res);

	}

}
