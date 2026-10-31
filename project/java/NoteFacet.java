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
  A note facet is a grouping of characteristics unique to a brief textual record.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NoteFacet extends Facet {

  private ObservableObject application;
  private ZonedDateTime observableCreatedTime;
  private ZonedDateTime observableModifiedTime;
  private String text;


}