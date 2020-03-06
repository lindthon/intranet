import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import { BlogComponent } from './blog/blog.component';
import { BlogSingleComponent } from './blog-single/blog-single.component';
import { BrowsejobsComponent } from './browsejobs/browsejobs.component';
import { CandidatesComponent } from './candidates/candidates.component';
import { ContactComponent } from './contact/contact.component';
import { JobPostComponent } from './job-post/job-post.component';
import { NewPostComponent } from './new-post/new-post.component';

@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    BlogComponent,
    BlogSingleComponent,
    BrowsejobsComponent,
    CandidatesComponent,
    ContactComponent,
    JobPostComponent,
    NewPostComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
