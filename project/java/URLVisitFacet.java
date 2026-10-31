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
  A URL visit facet is a grouping of characteristics unique to the properties of a visit of a URL within a particular browser.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URLVisitFacet extends Facet {

  private ObservableObject browserInformation;
  private ObservableObject fromURLVisit;
  private ObservableObject url;
  private String urlTransitionType;
  private String visitDuration;
  private ZonedDateTime visitTime;


}