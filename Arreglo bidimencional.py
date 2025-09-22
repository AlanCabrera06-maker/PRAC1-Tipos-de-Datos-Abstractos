# python
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

ventas = [[0 for _ in range(len(departamentos))] for _ in range(len(meses))]

def insertar_venta(mes, depto, cantidad):
    i = meses.index(mes)
    j = departamentos.index(depto)
    ventas[i][j] = cantidad

def buscar_venta(mes, depto):
    i = meses.index(mes)
    j = departamentos.index(depto)
    return ventas[i][j]

def eliminar_venta(mes, depto):
    i = meses.index(mes)
    j = departamentos.index(depto)
    ventas[i][j] = 0

insertar_venta("Enero", "Ropa", 1500)
insertar_venta("Febrero", "Deportes", 2500)

print("Venta en Enero de Ropa:", buscar_venta("Enero", "Ropa"))

eliminar_venta("Enero", "Ropa")
print("Venta eliminada, Enero de Ropa:", buscar_venta("Enero", "Ropa"))


# java
public class Ventas {

    static String[] meses = {"Enero","Febrero","Marzo","Abril","Mayo","Junio",
                             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};
    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};

    static int[][] ventas = new int[12][3];

    public static void insertarVenta(String mes, String depto, int cantidad) {
        int i = getMesIndex(mes);
        int j = getDeptoIndex(depto);
        ventas[i][j] = cantidad;
    }

    public static int buscarVenta(String mes, String depto) {
        int i = getMesIndex(mes);
        int j = getDeptoIndex(depto);
        return ventas[i][j];
    }

    public static void eliminarVenta(String mes, String depto) {
        int i = getMesIndex(mes);
        int j = getDeptoIndex(depto);
        ventas[i][j] = 0;
    }

    private static int getMesIndex(String mes) {
        for (int i = 0; i < meses.length; i++) {
            if (meses[i].equalsIgnoreCase(mes)) {
                return i;
            }
        }
        return -1;
    }

    private static int getDeptoIndex(String depto) {
        for (int j = 0; j < departamentos.length; j++) {
            if (departamentos[j].equalsIgnoreCase(depto)) {
                return j;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        insertarVenta("Enero", "Ropa", 1500);
        insertarVenta("Febrero", "Deportes", 2500);

        System.out.println("Venta en Enero de Ropa: " + buscarVenta("Enero", "Ropa"));

        eliminarVenta("Enero", "Ropa");
        System.out.println("Venta eliminada, Enero de Ropa: " + buscarVenta("Enero", "Ropa"));
    }
}