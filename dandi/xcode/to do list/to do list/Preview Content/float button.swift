//import SwiftUI
//
//struct ContentView: View {
//    var body: some View {
//        ZStack {
//            ScrollView {
//                VStack(spacing: 20) {
//                    ForEach(0..<50) { index in
//                        Text("Item \(index)")
//                            .frame(maxWidth: .infinity)
//                            .padding()
//                            .background(Color.gray.opacity(0.2))
//                            .cornerRadius(8)
//                    }
//                }
//                .padding()
//            }
//
//            // 고정된 버튼
//            VStack {
//                Spacer()
//                HStack {
//                    Spacer()
//                    Button(action: {
//                        
//                        print("Floating Button Tapped")
//                    }) {
//                        Image(systemName: "plus")
//                            .font(.system(size: 24))
//                            .padding()
//                            .background(Color.blue)
//                            .foregroundColor(.white)
//                            .clipShape(Circle())
//                            .shadow(radius: 5)
//                    }
//                    .padding()
//                }
//            }
//        }
//    }
//}
