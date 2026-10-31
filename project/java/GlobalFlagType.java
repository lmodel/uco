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
  A global flag type is a grouping of characteristics unique to the Windows systemwide global variable named NtGlobalFlag that enables various internal debugging, tracing, and validation support in the operating system. [based on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals by Solomon, Russinovich, and Ionescu]
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GlobalFlagType extends UcoInherentCharacterizationThing {

  private String abbreviation;
  private String destination;
  private List<String> hexadecimalValue;
  private String symbolicName;


}