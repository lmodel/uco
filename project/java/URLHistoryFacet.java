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
  A URL history facet is a grouping of characteristics unique to the stored URL history for a particular web browser
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class URLHistoryFacet extends Facet {

  private ObservableObject browserInformation;
  private List<URLHistoryEntry> urlHistoryEntry;


}