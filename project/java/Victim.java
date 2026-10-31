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
  A victim is a role played by a person or organization that is/was the target of some malicious action.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Victim extends NeutralRole {



}