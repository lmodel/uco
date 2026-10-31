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
  A mime part type is a grouping of characteristics unique to a component of a multi-part email body.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MimePartType extends UcoInherentCharacterizationThing {

  private String body;
  private ObservableObject bodyRaw;
  private String contentDisposition;
  private String contentType;


}