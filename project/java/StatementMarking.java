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
  A statement marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement markings are generally not machine-readable. An example of this would be a simple marking to apply copyright information, such as 'Copyright 2014 Acme Inc.'.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatementMarking extends MarkingModel {

  private List<String> definitionType;
  private String markingStatement;


}