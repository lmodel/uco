package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A browser bookmark facet is a grouping of characteristics unique to a saved shortcut that directs a WWW (World Wide Web) browser software program to a particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class BrowserBookmarkFacet extends Facet {

  private ZonedDateTime accessedTime;
  private ObservableObject application;
  private String bookmarkPath;
  private ZonedDateTime observableCreatedTime;
  private ZonedDateTime observableModifiedTime;
  private List<URI> urlTargeted;
  private Integer visitCount;


}