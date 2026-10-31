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
  An IComHandler action type is a grouping of characteristics unique to a Windows Task-related action that fires a Windows COM handler (smart code in the client address space that can optimize calls between a client and server). [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IComHandlerActionType extends UcoInherentCharacterizationThing {

  private String comClassID;
  private String comData;


}