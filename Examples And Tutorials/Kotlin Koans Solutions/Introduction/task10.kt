import java.util.Collections
import java.util.Comparator


fun getList(): List<Int> {
    val arrayList = arrayListOf(1, 5, 2)
    Collections.sort(arrayList, object: Comparator<Int> {
        public override fun compare(n0: Int, n1: Int): Int {
            return n1 - n0
        }
    })
    return arrayList
}
