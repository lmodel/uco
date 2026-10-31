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
  A message facet is a grouping of characteristics unique to a discrete unit of electronic communication intended by the source for consumption by some recipient or group of recipients. [based on https://en.wikipedia.org/wiki/Message]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MessageFacet extends Facet {

  private ObservableObject application;
  private ObservableObject from;
  private String messageID;
  private String messageText;
  private String messageType;
  private ZonedDateTime sentTime;
  private String sessionID;
  private List<ObservableObject> to;


}