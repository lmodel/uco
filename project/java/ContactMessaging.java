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
  A contact messaging is a grouping of characteristics unique to details for contacting a contact entity by digital messaging.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactMessaging extends UcoInherentCharacterizationThing {

  private ObservableObject contactMessagingPlatform;
  private ObservableObject messagingAddress;


}