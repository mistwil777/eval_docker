import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { TodoItem } from '../models'

const URL = 'http://localhost:8000'

@Injectable({
  providedIn: 'root',
})
export class TodoItemsService {
  constructor(private http: HttpClient) {}
  
  getTodoItems() {
    return this.http.get<TodoItem[]>(`${URL}/todo_items`)
  }

  addTodoItem(todoItem: TodoItem) {
    return this.http.post<TodoItem>(`${URL}/todo_items`, todoItem)
  }
}
