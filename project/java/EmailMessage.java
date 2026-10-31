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
  An email message is a message that is an instance of an electronic mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EmailMessage extends Message {



}