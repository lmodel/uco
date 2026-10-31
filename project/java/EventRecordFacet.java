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
  An event record facet is a grouping of characteristics unique to something that happens in a digital context (e.g., operating system events).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EventRecordFacet extends Facet {

  private ObservableObject account;
  private ObservableObject application;
  private ObservableAction cyberAction;
  private String eventID;
  private ObservableObject eventRecordDevice;
  private String eventRecordID;
  private String eventRecordRaw;
  private String eventRecordServiceName;
  private String eventRecordText;
  private ZonedDateTime observableCreatedTime;
  private ZonedDateTime observableEndTime;
  private String observableEventType;
  private ZonedDateTime observableStartTime;


}