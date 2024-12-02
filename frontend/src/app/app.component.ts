import { Component } from '@angular/core';
import { NavbarComponent } from "./shared/navbar/navbar.component";
import { FooterComponent } from './shared/footer/footer.component'
import { TodoItemsService } from './core/services/todo_items.service';
import { Observable, of, shareReplay, Subscription } from 'rxjs';
import { TodoItem } from './core/models';
import { AsyncPipe } from '@angular/common';
import { DataViewModule } from 'primeng/dataview';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NavbarComponent, FooterComponent, AsyncPipe, DataViewModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  subscriptions = new Subscription()

  todoItems$: Observable<TodoItem[]> = of()

  constructor(private todoItemsService: TodoItemsService) {
    this.todoItems$ = this.todoItemsService.getTodoItems().pipe(shareReplay())
  }

  ngOnDestroy() {
    this.subscriptions.unsubscribe()
  }
}
