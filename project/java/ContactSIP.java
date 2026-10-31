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
  A contact SIP is a grouping of characteristics unique to details for contacting a contact entity by Session Initiation Protocol (SIP).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactSIP extends UcoInherentCharacterizationThing {

  private String contactSIPScope;
  private ObservableObject sipAddress;


}