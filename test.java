import java.util.List;

public class test {
    public static void main(String[] args) {
        String [] data = new String [] {"path=[GeoPoint {latitude=37.49927449084337", "longitude=127.02321559321373 }", "GeoPoint {latitude=37.49980829567853", "longitude=127.02298834539994 }", "GeoPoint {latitude=37.49991358823846", "longitude=127.02293920721507 }"};
        String [] H = new String[] {"[3]여성안전지킴이집=[36.82524646", "128.6297047]", "[2]여성안전지킴이집=[36.82505084", "128.6327065]", "[1]여성안전지킴이집=[36.82751754", "128.6312936]" };

        String lat;
        String lon;
        for (int i = 0; i < H.length; i++){
            if (i%2 == 0){
                lat = H[i].split("=")[1].substring(1, H[i].split("=")[1].length());
                System.out.println(lat);
            }
            else {
                lon = H[i].substring(0, H[i].length()-1);
                System.out.println(lon);
            }
        }

        
    }
}
