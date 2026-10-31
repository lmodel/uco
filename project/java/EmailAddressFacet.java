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
  An email address facet is a grouping of characteristics unique to an identifier for an electronic mailbox to which electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EmailAddressFacet extends DigitalAddressFacet {



}