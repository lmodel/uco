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
  A contact address is a grouping of characteristics unique to a geolocation address of a contact entity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContactAddress extends UcoInherentCharacterizationThing {

  private String contactAddressScope;
  private Location geolocationAddress;


}