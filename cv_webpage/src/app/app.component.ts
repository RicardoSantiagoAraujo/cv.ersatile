import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

// PrimeNG
import { ButtonModule } from 'primeng/button';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ButtonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'cv_webpage';
}
