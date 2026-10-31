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
  A person is a grouping of identifying characteristics unique to a human being regarded as an individual. [based on https://www.lexico.com/en/definition/person]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Person extends Identity {



}