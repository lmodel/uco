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
  An attributed name is a name of an entity issued by some attributed naming authority.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttributedName extends UcoObject {

  private String namingAuthority;


}