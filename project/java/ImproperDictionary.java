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
  UCO 1.5.0 declares the class uco-types:ImproperDictionary without a definition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImproperDictionary extends Dictionary {

  private List<String> repeatsKey;


}