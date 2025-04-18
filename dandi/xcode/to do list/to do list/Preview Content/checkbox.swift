//import SwiftUI
//
//struct ListItem: Identifiable {
//    let id = UUID()
//    let title: String
//    var isChecked: Bool
//}
//
//struct ContentView: View {
//    @State private var items: [ListItem] = [
//        ListItem(title: "사과", isChecked: false),
//        ListItem(title: "바나나", isChecked: true),
//        ListItem(title: "오렌지", isChecked: false),
//        ListItem(title: "포도", isChecked: false)
//    ]
//
//    var body: some View {
//        List {
//            ForEach($items) { $item in
//                HStack {
//                    Button(action: {
//                        item.isChecked.toggle()
//                    }) {
//                        Image(systemName: item.isChecked ? "checkmark.square" : "square")
//                            .foregroundColor(item.isChecked ? .blue : .gray)
//                    }.buttonStyle(border)
//
//                    Text(item.title)
//                        .strikethrough(item.isChecked, color: .gray)
//                        .foregroundColor(item.isChecked ? .gray : .primary)
//                }
//                .padding(.vertical, 4)
//            }
//        }
//    }
//}
////