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
  An online service facet is a grouping of characteristics unique to a particular provision mechanism of information access, distribution or manipulation over the Internet.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OnlineServiceFacet extends Facet {

  private List<ObservableObject> inetLocation;
  private String name;
  private List<Location> observableLocation;


}