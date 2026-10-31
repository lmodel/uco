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
  A calendar facet is a grouping of characteristics unique to a collection of appointments, meetings, and events.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalendarFacet extends Facet {

  private ObservableObject application;
  private UcoObject owner;


}