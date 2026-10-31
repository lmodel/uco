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
  A grouping is a compilation of referenced UCO content with a shared context.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Grouping extends ContextualCompilation {

  private List<String> context;


}