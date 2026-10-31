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
  A Windows PE section is a grouping of characteristics unique to a specific default or custom-defined region of a Windows PE (Portable Executable) file, consisting of an individual portion of the actual executable content of the file delineated according to unique purpose and memory protection requirements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class WindowsPESection extends UcoInherentCharacterizationThing {

  private BigDecimal entropy;
  private List<Hash> hashes;
  private String name;
  private Integer size;


}