////
////  ContentView.swift
////  lowbar
////
////  Created by maple on 4/15/25.
////
//
//import SwiftUI
//
//
//struct ContentView: View {
//    @State private var fruit : [String] = ["apple","orange","banana"]
//    var body: some View {
//        List{
//            Section{
//                ForEach(fruit,id:\.self){fruit in
//                    HStack{
//                        Text(fruit)
//                        Spacer()
//                        Button(action:{
//                            delete(fruit)
//                        }){
//                            Image(systemName: "trash.fill")
//                                .foregroundColor(.gray)
//                        }.buttonStyle(BorderlessButtonStyle())
//                    }
//                    
//                }
//            }
//        }
//    }
//    func delete(_ item:String){
//        if let index = fruit.firstIndex(of: item){
//            fruit.remove(at:index)
//        }
//    }
//}
//
//#Preview {
//    ContentView()
//}
////
