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
  A controlled vocabulary is an explicitly constrained set of string values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlledVocabulary extends UcoObject {

  private String constrainingVocabularyName;
  private URI constrainingVocabularyReference;
  private String value;


}