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
  A call facet is a grouping of characteristics unique to a connection as part of a realtime cyber communication between one or more parties.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CallFacet extends Facet {

  private ObservableObject application;
  private String callType;
  private Integer duration;
  private ObservableObject from;
  private ZonedDateTime observableEndTime;
  private List<ObservableObject> observableParticipant;
  private ZonedDateTime observableStartTime;
  private List<ObservableObject> to;


}