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
  A Windows PE file header is a grouping of characteristics unique to the 'header' of a Windows PE (Portable Executable) file, consisting of a collection of metadata about the overall nature and structure of the file.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsPEFileHeader extends UcoInherentCharacterizationThing {

  private ZonedDateTime timeDateStamp;


}