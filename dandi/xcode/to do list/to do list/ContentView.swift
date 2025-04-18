import SwiftUI

// 리스트 항목 모델
struct ListItem: Hashable {
    var title: String
    var Ischecked: Bool
    var date : Date
}

struct ContentView: View {
    
    @State private var showsheet = false
    @State private var fruit: [ListItem] = []
    @State private var inputtext = ""
    @State private var selectDate: Date = Date()
    
    var body: some View {
        ZStack {
            VStack {
                HStack{
                    Text("To do list")
                        .font(.title)
                        .bold()
                        .foregroundColor(.blue)
                        .multilineTextAlignment(.trailing)
                    Spacer().frame(width: 50)
                    Text(formattedToday())
                    
                    
                }
                List {
                    ForEach(fruit.indices, id: \.self) { index in
                        HStack {
                            
                            Button(action: {
                                fruit[index].Ischecked.toggle()
                            }) {
                                Image(systemName: fruit[index].Ischecked ? "checkmark.circle.fill" : "circle")
                                    .foregroundColor(fruit[index].Ischecked ? .gray : .blue)
                            }
                            .buttonStyle(PlainButtonStyle())
                            
                            Text(fruit[index].title)
                                .strikethrough(fruit[index].Ischecked, color: .gray)// ischecked 여부에 따라 회색 취소선 생성
                                .foregroundColor(fruit[index].Ischecked ? .gray : .primary)// 같은 경우에 회색으로 글자색 변경
                            
                            Spacer()
                            
                 
                            Button(action: {
                                delete(fruit[index])
                            }) {
                                Image(systemName: "trash.fill")
                                    .foregroundColor(.gray)
                            }
                            .buttonStyle(BorderlessButtonStyle())
                        }
                    }
                }
            }
            .sheet(isPresented: $showsheet) {
                BottomSheetView(text: $inputtext) { newItem in
                    if !newItem.title.isEmpty {
                        fruit.append(newItem)
                        inputtext = ""
                    }
                }
                .presentationDetents([.height(120), .large])
                .presentationDragIndicator(.hidden)
            }
            
          
            VStack {
                Spacer()
                HStack {
                    Spacer()
                    Button(action: {
                        showsheet = true
                    }) {
                        Image(systemName: "plus")
                            .font(.system(size: 24))
                            .padding()
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .clipShape(Circle())
                            .shadow(radius: 5)
                    }
                    .padding()
                }
            }
        }
    }
    func formattedToday() -> String {
        let formatter = DateFormatter()
        formatter.locale = Locale(identifier: "ko_KR")
        formatter.dateFormat = "yyyy. M. d. (E)" //
        return formatter.string(from: Date())
    }

    
    
    func delete(_ item: ListItem) {
        if let index = fruit.firstIndex(of: item) {
            fruit.remove(at: index)
        }
    }
}


struct BottomSheetView: View {
    @Binding var text: String
    @Environment(\.dismiss) var dismiss
    @State private var selectedDate: Date = Date()

    var onAdd: (ListItem) -> Void
    
    var body: some View {
        VStack(spacing: 20) {
            Text("오늘 할 일")
                .font(.title2)
            HStack {
                TextField("계획 작성", text: $text)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding(.horizontal)
                    .onSubmit {
                        if !text.isEmpty{
                            onAdd(ListItem(title: text, Ischecked: false,date: selectedDate))
                            dismiss()
                        }
                    }
                
//                Button(action: {
//                    onAdd(ListItem(title: text, Ischecked: false))
//                    dismiss()
//                }) {
//                    Image(systemName: "plus.app")
//                        .resizable()
//                        .frame(width: 30, height: 30)
//                }
//                .disabled(text.isEmpty)
            }
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
