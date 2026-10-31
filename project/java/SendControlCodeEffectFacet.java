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
  A send control code effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a control code, or other control-oriented communication signal, is sent to the observable object. An example of this would be an action sending a control code changing the running state of a process.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SendControlCodeEffectFacet extends DefinedEffectFacet {

  private String controlCode;


}