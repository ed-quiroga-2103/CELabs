import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  eventSource: any[];
 // events: [{ title: 'Event 1 ', startTime: 'Sun Aug 16 2020 18:00:00 GMT-0600 
 // (Central Standard Time)', endTime:
 // 'Sun Aug 16 2020 20:00:00 GMT-0600 (Central Standard Time)',
 // allDay: false}];
  viewTitle: any;
  isToday: boolean;
  calendar = {
      mode: 'week',
      currentDate: new Date(),
  };
    lockSwipeToPrev: boolean;
    Time = 'Time';
  constructor() {}

  loadEvents() {
    this.eventSource = this.createRandomEvents();
}
onViewTitleChanged(title: any) {
    this.viewTitle = title;
}
onEventSelected(event: { startTime: string; endTime: string; title: string; }) {
    console.log('Evento seleccionado:' + event.startTime + '-' + event.endTime + ',' + event.title);
}
changeMode(mode: string) {
    this.calendar.mode = mode;
}
today() {
    this.calendar.currentDate = new Date();
}
onTimeSelected(ev: { selectedTime: string; events: string | any[]; disabled: string; }) {
    console.log('Hora seleccionada: ' + ev.selectedTime + ', hasEvents: ' +
        (ev.events !== undefined && ev.events.length !== 0) + ', disabled: ' + ev.disabled);
    this.changeMode('week');
}
onCurrentDateChanged(event: Date) {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    event.setHours(0, 0, 0, 0);
    this.isToday = today.getTime() === event.getTime();

    if (this.calendar.mode === 'month') {
        if (event.getFullYear() < today.getFullYear() ||
        (event.getFullYear() === today.getFullYear() && event.getMonth() <= today.getMonth())) {
            this.lockSwipeToPrev = true;
        } else {
            this.lockSwipeToPrev = false;
        }
    }
}
createRandomEvents() {
    const events = [];
    for (let i = 0; i < 50; i += 1) {
        const date = new Date();
        const eventType = Math.floor(Math.random() * 2);
        const startDay = Math.floor(Math.random() * 90) - 45;
        let endDay = Math.floor(Math.random() * 2) + startDay;
        let startTime: Date;
        let endTime: Date;
        if (eventType === 0) {
            startTime = new Date(Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate() + startDay));
            console.log('startTime');
            if (endDay === startDay) {
                endDay += 1;
            }
            endTime = new Date(Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate() + endDay));
            events.push({
                title: 'All Day - ' + i,
                startTime,
                endTime,
                allDay: true
            });
        } else {
            const startMinute = Math.floor(Math.random() * 24 * 60);
            const endMinute = Math.floor(Math.random() * 180) + startMinute;
            startTime = new Date(date.getFullYear(), date.getMonth(), date.getDate() + startDay, 0, date.getMinutes() + startMinute);
            endTime = new Date(date.getFullYear(), date.getMonth(), date.getDate() + endDay, 0, date.getMinutes() + endMinute);
            events.push({
                title: 'Event - ' + i,
                startTime,
                endTime,
                allDay: false
            });
        }
    }
    console.log(events);
    return events;
}
onRangeChanged(ev: { startTime: string; endTime: string; }) {
    console.log('range changed: startTime: ' + ev.startTime + ', endTime: ' + ev.endTime);
}
markDisabled = (date: Date) => {
    const current = new Date();
    current.setHours(0, 0, 0);
    return date < current;
}

next() {
    // tslint:disable-next-line: no-string-literal
    const swiper = document.querySelector('.swiper-container')['swiper'];
    swiper.slideNext();
  }
  back() {
    // tslint:disable-next-line: no-string-literal
    const swiper = document.querySelector('.swiper-container')['swiper'];
    swiper.slidePrev();
  }

}
