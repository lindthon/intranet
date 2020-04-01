import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CategoriaNoticiasComponent } from './categoria-noticias.component';

describe('CategoriaNoticiasComponent', () => {
  let component: CategoriaNoticiasComponent;
  let fixture: ComponentFixture<CategoriaNoticiasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CategoriaNoticiasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CategoriaNoticiasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
