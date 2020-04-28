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

}
/*
 import {MdbTableDirective} from "PATH-TO-MDB-ANGULAR"; @Component({ selector:
'search-table', templateUrl: './search-table.component.html', styleUrls:
['./search-table.component.scss'] }) export class SearchTableComponent {
@ViewChild(MdbTableDirective, { static: true }) mdbTable:
MdbTableDirective; elements: any = []; headElements = ['ID', 'First',
'Last', 'Handle']; searchText: string = ''; previous: string;
constructor() { } @HostListener('input') oninput() { this.searchItems();
} ngOnInit() { for (let i = 1; i <= 10; i++) { this.elements.push({ id:
i.toString(), first: 'Wpis' + (Math.floor(Math.random() * i *
10)).toString(), last: 'Last' + (Math.floor(Math.random() * i *
10)).toString(), handle: 'Handle' + (Math.floor(Math.random() * i *
10)).toString() }); } this.mdbTable.setDataSource(this.elements);
this.previous = this.mdbTable.getDataSource(); } searchItems() { const
prev = this.mdbTable.getDataSource(); if (!this.searchText) {
this.mdbTable.setDataSource(this.previous); this.elements =
this.mdbTable.getDataSource(); } if (this.searchText) { this.elements =
this.mdbTable.searchLocalDataByMultipleFields(this.searchText, ['first',
'last']); this.mdbTable.setDataSource(prev); } } }*/