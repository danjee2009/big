import SwiftUI

// 리스트 항목 모델
struct ListItem: Hashable {//di:\.self 사용 가능을 위해
    var title: String //화면에 표시될 텍스트
    var Ischecked: Bool //체크여부를 불형태로 정해 true/false에 따른 동작을 설정
    var date : Date
}

struct ContentView: View {
    
    @State private var showsheet = false
    @State private var fruit: [ListItem] = []
    @State private var inputtext = ""
    @State private var selectDate: Date = Date()
    
    var body: some View {
        ZStack {// 플로팅 버튼때문에
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
                            //체크박스 부분
                            Button(action: {
                                fruit[index].Ischecked.toggle()
                            }) {
                                Image(systemName: fruit[index].Ischecked ? "checkmark.circle.fill" : "circle")
                                    .foregroundColor(fruit[index].Ischecked ? .gray : .blue)//ischecked의 상태에 따라 true-gray, false-blue의 색을 띄게 함
                            }
                            .buttonStyle(PlainButtonStyle())//사용자 설정에 따라 버튼의 형태 변경 가능/눌릴시 반응 설정
                            
                            //계획 텍스트 부분
                            Text(fruit[index].title)
                                .strikethrough(fruit[index].Ischecked, color: .gray)// ischecked 여부에 따라 회색 취소선 생성
                                .foregroundColor(fruit[index].Ischecked ? .gray : .primary)// 같은 경우에 회색으로 글자색 변경
                            
                            Spacer()
                            
                            //삭제 버튼 부분
                            Button(action: {
                                delete(fruit[index])
                            }) {
                                Image(systemName: "trash.fill")
                                    .foregroundColor(.gray)
                            }
                            .buttonStyle(BorderlessButtonStyle())//버튼 이외의 영역에 상호작용X
                        }
                    }
                }
            }
            .sheet(isPresented: $showsheet) {//시트
                BottomSheetView(text: $inputtext) { newItem in
                    if !newItem.title.isEmpty {
                        fruit.append(newItem)
                        inputtext = ""
                    }
                }
                .presentationDetents([.height(120), .large])//임의높이, 전체 높이
                .presentationDragIndicator(.hidden)//dragindicator 숨기기
            }
            
            // ✅ 플로팅 버튼
            VStack {//zstack으로 개별적인 버튼을 생성(list는 자체적으로 스크롤기능이 있기 때문)
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
        formatter.dateFormat = "yyyy. M. d. (E)" // 예: 2025. 4. 17. (목)
        return formatter.string(from: Date())
    }

    
    // 삭제 함수
    func delete(_ item: ListItem) {
        if let index = fruit.firstIndex(of: item) {
            fruit.remove(at: index)
        }
    }
}

// ✅ 바텀 시트: 항목 추가용
struct BottomSheetView: View {
    @Binding var text: String//상위 뷰의 텍스트 값을 바인딩해 사용
    @Environment(\.dismiss) var dismiss//시트창 닫기 기능
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
                    .onSubmit {//엔터로 항목 추가
                        if !text.isEmpty{//빈 항목 추가 방지
                            onAdd(ListItem(title: text, Ischecked: false,date: selectedDate))
                            dismiss()
                        }
                    }
                
//                Button(action: {//버튼을 눌러 항목 추가
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
