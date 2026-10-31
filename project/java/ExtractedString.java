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
  An extracted string is a grouping of characteristics unique to a series of characters pulled from an observable object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExtractedString extends UcoInherentCharacterizationThing {

  private String byteStringValue;
  private String encoding;
  private String englishTranslation;
  private String language;
  private Integer length;
  private String stringValue;


}