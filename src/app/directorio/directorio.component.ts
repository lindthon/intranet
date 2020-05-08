import { Component,HostListener,ViewChild, OnInit } from '@angular/core';

@Component({
  selector: 'app-directorio',
  templateUrl: './directorio.component.html',
  styleUrls: ['./directorio.component.css']
})
export class DirectorioComponent implements OnInit {


  constructor() { }

  ngOnInit(): void {
  }
   settings = {
    actions: {
      delete: false,
      add: false,
      edit:false,      
    },
    columns: {
      
      name: {
        title: 'Full Name',
      },      
      email: {
        title: 'Email',
      },
      office: {
        title: 'Oficina',
      },
      ext: {
        title: 'Extension',
      }
    },
  };

  data = [
    {
      id: 1,
      name: "Leanne Graham",      
      email: "Sincere@april.biz",
      office:"Planta 1",
      ext:"256"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Planta 1",
      ext:"255"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Planta 2",
      ext:"128"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Oficina Centro",
      ext:"222"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Planta 1",
      ext:"222"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Planta 1",
      ext:"222"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Planta 2",
      ext:"222"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Planta 2",
      ext:"222"
    },
    {
      id: 1,
      name: "Leanne Graham",
      username: "Bret",
      email: "Sincere@april.biz",
      office:"Oficina Centro",
      ext:"222"
    },
    {
      id: 2,
      name: "Ervin Howell",
      username: "Antonette",
      email: "Shanna@melissa.tv",
      office:"Oficina Centro",
      ext:"222"
    },

    // ... list of items
  ];

  onDeleteConfirm(event) {
    console.log("Delete Event In Console")
    console.log(event);
    if (window.confirm('Are you sure you want to delete?')) {
      event.confirm.resolve();
    } else {
      event.confirm.reject();
    }
  }

  onCreateConfirm(event) {
    console.log("Create Event In Console")
    console.log(event);

  }

  onSaveConfirm(event) {
    console.log("Edit Event In Console")
    console.log(event);
  }
  

}
