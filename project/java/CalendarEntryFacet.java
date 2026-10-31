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
  A calendar entry facet is a grouping of characteristics unique to an appointment, meeting, or event within a collection of appointments, meetings, and events.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CalendarEntryFacet extends Facet {

  private ObservableObject application;
  private List<Identity> attendant;
  private Integer duration;
  private String eventStatus;
  private Boolean isPrivate;
  private ZonedDateTime observableCreatedTime;
  private ZonedDateTime observableEndTime;
  private String observableEventType;
  private Location observableLocation;
  private ZonedDateTime observableModifiedTime;
  private ZonedDateTime observableStartTime;
  private UcoObject owner;
  private String recurrence;
  private ZonedDateTime remindTime;
  private String subject;


}