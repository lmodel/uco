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
  An environment variable is a grouping of characteristics unique to a dynamic-named value that can affect the way running processes will behave on a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class EnvironmentVariable extends UcoInherentCharacterizationThing {

  private String name;
  private String observableValue;


}