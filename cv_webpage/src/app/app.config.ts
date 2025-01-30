import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';

// PrimeNG
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { providePrimeNG } from 'primeng/config';
import Aura from '@primeng/themes/aura';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideClientHydration(),
    // PrimeNG
    provideAnimationsAsync(),
    providePrimeNG({
        theme: {
            preset: Aura, //Aura, Material, Lara and Nora
            options: {
              darkModeSelector: '.my-app-dark'
            }
        },
        ripple: true // Ripple is an optional animation for the supported components such as buttons
    })
  ]
};
