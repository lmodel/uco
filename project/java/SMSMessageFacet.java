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
  A SMS message facet is a grouping of characteristics unique to a message conformant to the short message service (SMS) communication protocol standards.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SMSMessageFacet extends Facet {

  private Boolean isRead;


}