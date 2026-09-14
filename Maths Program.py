import pygame
import sys
import random

pygame.init()
WHITE = (255, 255, 255)


#for quizzing game

questions = [
    {"question": "quizzing game/q (1).png", "answers": ["quizzing game/q (1) correct ans.jpg", "quizzing game/q (1) ans 2.jpg", "quizzing game/q (1) ans 3.jpg", "quizzing game/q (1) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (2).png", "answers": ["quizzing game/q (2) correct ans.jpg", "quizzing game/q (2) ans 2.jpg", "quizzing game/q (2) ans 3.jpg", "quizzing game/q (2) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (3).png", "answers": ["quizzing game/q (3) correct ans.jpg", "quizzing game/q (3) ans 2.jpg", "quizzing game/q (3) ans 3.jpg", "quizzing game/q (3) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (4).png", "answers": ["quizzing game/q (4) correct ans.jpg", "quizzing game/q (4) ans 2.jpg", "quizzing game/q (4) ans 3.jpg", "quizzing game/q (4) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (5).png", "answers": ["quizzing game/q (5) correct ans.jpg", "quizzing game/q (5) ans 2.jpg", "quizzing game/q (5) ans 3.jpg", "quizzing game/q (5) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (6).png", "answers": ["quizzing game/q (6) correct ans.jpg", "quizzing game/q (6) ans 2.jpg", "quizzing game/q (6) ans 3.jpg", "quizzing game/q (6) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (7).png", "answers": ["quizzing game/q (7) correct ans.jpg", "quizzing game/q (7) ans 2.jpg", "quizzing game/q (7) ans 3.jpg", "quizzing game/q (7) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (8).png", "answers": ["quizzing game/q (8) correct ans.jpg", "quizzing game/q (8) ans 2.jpg", "quizzing game/q (8) ans 3.jpg", "quizzing game/q (8) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (9).png", "answers": ["quizzing game/q (9) correct ans.jpg", "quizzing game/q (9) ans 2.jpg", "quizzing game/q (9) ans 3.jpg", "quizzing game/q (9) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (10).png", "answers": ["quizzing game/q (10) correct ans.jpg", "quizzing game/q (10) ans 2.jpg", "quizzing game/q (10) ans 3.jpg", "quizzing game/q (10) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (11).png", "answers": ["quizzing game/q (11) correct ans.jpg", "quizzing game/q (11) ans 2.jpg", "quizzing game/q (11) ans 3.jpg", "quizzing game/q (11) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (12).png", "answers": ["quizzing game/q (12) correct ans.jpg", "quizzing game/q (12) ans 2.jpg", "quizzing game/q (12) ans 3.jpg", "quizzing game/q (12) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (13).png", "answers": ["quizzing game/q (13) correct ans.jpg", "quizzing game/q (13) ans 2.jpg", "quizzing game/q (13) ans 3.jpg", "quizzing game/q (13) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (14).png", "answers": ["quizzing game/q (14) correct ans.jpg", "quizzing game/q (14) ans 2.jpg", "quizzing game/q (14) ans 3.jpg", "quizzing game/q (14) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (15).png", "answers": ["quizzing game/q (15) correct ans.jpg", "quizzing game/q (15) ans 2.jpg", "quizzing game/q (15) ans 3.jpg", "quizzing game/q (15) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (16).png", "answers": ["quizzing game/q (16) correct ans.jpg", "quizzing game/q (16) ans 2.jpg", "quizzing game/q (16) ans 3.jpg", "quizzing game/q (16) ans 4.jpg"], "correct": 0},
    {"question": "quizzing game/q (17).png", "answers": ["quizzing game/q (17) correct ans.jpg", "quizzing game/q (17) ans 2.jpg", "quizzing game/q (17) ans 3.jpg", "quizzing game/q (17) ans 4.jpg"], "correct": 0}
    ]

for q in questions:
    q["questionIMG"] = pygame.image.load(q["question"])
    q["answersIMG"] = [pygame.image.load(answer) for answer in q["answers"]]
    

# variables for quizzing game:

current_question = 0
selected_ans = None
attempts = 0
score = 0


# function for shuffling answer positions (quizzing game)

def shuffle_answers (q_data):
    answers = q_data["answersIMG"]
    correct_index = q_data["correct"]

    ans_pairs = list(enumerate(answers))
    random.shuffle(ans_pairs)

    q_data["answersIMG"] = [pair[1] for pair in ans_pairs]
    q_data["correct"] = [pair[0] for pair in ans_pairs].index(correct_index)



# displaying/ generating the game window

screen = pygame.display.set_mode((1000, 630))


# MAIN page variables for program, and images

main_menu_writing = pygame.image.load("main menu writing.png")

MainMenu = "main menu"
RevisionNotes_Page = "rev_notes"
GamePage = "Game"
GameOverPage = "GameOver"
CurrentPage = MainMenu

# game buttons, images

game_over_page = pygame.image.load("GAMEOVER screen.png")

game_button_image = pygame.image.load("game button.png")
game_button = game_button_image.get_rect(topleft=(302, 330))

retry_button_image = pygame.image.load("RetryButton.png")
retry_button = retry_button_image.get_rect(topleft=(165, 330))

M_menu_button_image = pygame.image.load("MainMenuButton.png")
M_menu_button = M_menu_button_image.get_rect(topleft=(500, 330))

# font for score text

font = pygame.font.Font("half_bold_pixel-7.ttf", 85)

score_text = font.render(str(score), True, WHITE)
scorewriting = font.render("Score:", True, WHITE)


# revision notes buttons

rev_button_image = pygame.image.load("revisionnotes_button.png")
rev_button = rev_button_image.get_rect(topleft=(302, 510))

KS4_rev_notes_title = pygame.image.load("KS4_rev_notes.png")

back_button_image = pygame.image.load("backbutton.png")
back_button = back_button_image.get_rect(topleft = (5, 550))

topic_pg_back_button_IMG = pygame.image.load("topic pge back button.png")
topic_pg_back_button = topic_pg_back_button_IMG.get_rect(topleft=(320, 574))

left_button_IMG = pygame.image.load("left button.png")
previous_button = left_button_IMG.get_rect(topleft = (12,576))

right_button_IMG = pygame.image.load("right button.png")
next_button = right_button_IMG.get_rect(topleft = (950, 576))

# health bar images

HB_3 = pygame.image.load("HealthBar_3.png")
HB_2 = pygame.image.load("HealthBar_2.png")
HB_1 = pygame.image.load("HealthBar_1.png")
HB_IMG = HB_3


# revision notes section - each of the loaded images for the buttons, and the images of the notes themselves

KS4_topics_pages ={
    "numbers_page": pygame.image.load("KS4 topics/pages/numbers_page.png"),
    "algebra_page": pygame.image.load("KS4 topics/pages/algebra_page.png"),
    "geometry_page": pygame.image.load("KS4 topics/pages/geometry_page.png"),
    "probability_page": pygame.image.load("KS4 topics/pages/probability_page.png"),
    "ratio_page": pygame.image.load("KS4 topics/pages/ratio_page.png"),
    "graphs_page": pygame.image.load("KS4 topics/pages/graphs_page.png")
}


KS4_buttons= [
    (pygame.image.load("KS4 topics/Numbers.png"), pygame.image.load("KS4 topics/Numbers.png").get_rect(center=(250,185)), "numbers_page"),
    (pygame.image.load("KS4 topics/Algebra.png"), pygame.image.load("KS4 topics/Algebra.png").get_rect(center=(750,185)), "algebra_page"),
    (pygame.image.load("KS4 topics/Geometry.png"), pygame.image.load("KS4 topics/Geometry.png").get_rect(center=(250,335)), "geometry_page"),
    (pygame.image.load("KS4 topics/Probability.png"), pygame.image.load("KS4 topics/Probability.png").get_rect(center=(750,335)), "probability_page"),
    (pygame.image.load("KS4 topics/Ratio.png"), pygame.image.load("KS4 topics/Ratio.png").get_rect(center=(250, 485)), "ratio_page"),
    (pygame.image.load("KS4 topics/Graphs.png"), pygame.image.load("KS4 topics/Graphs.png").get_rect(center=(750,485)), "graphs_page")
]

KS4_subtopic_buttons = {
    "numbers_page":[
        (pygame.image.load("subtopic buttons/numbers/types of num button.JPEG"), pygame.image.load("subtopic buttons/numbers/types of num button.JPEG").get_rect(center=(249,150)), "typesofnumbers_notes"),
        (pygame.image.load("subtopic buttons/numbers/rounding button.png"), pygame.image.load("subtopic buttons/numbers/rounding button.png").get_rect(center=(750,150)), "rounding_notes"),
        (pygame.image.load("subtopic buttons/numbers/place val button.png"), pygame.image.load("subtopic buttons/numbers/place val button.png").get_rect(center=(249,280)), "placeval_notes"),
        (pygame.image.load("subtopic buttons/numbers/fractions button.png"), pygame.image.load("subtopic buttons/numbers/fractions button.png").get_rect(center=(750,280)), "fractions_notes"),
        (pygame.image.load("subtopic buttons/numbers/BIDMAS button.png"), pygame.image.load("subtopic buttons/numbers/BIDMAS button.png").get_rect(center=(249,410)), "BIDMAS_notes"),
        (pygame.image.load("subtopic buttons/numbers/decimals button.png"), pygame.image.load("subtopic buttons/numbers/decimals button.png").get_rect(center=(750,410)), "decimals_notes"),
        (pygame.image.load("subtopic buttons/numbers/FDP button.png"), pygame.image.load("subtopic buttons/numbers/FDP button.png").get_rect(center=(500,540)), "FDP_notes")
         ],

    "algebra_page": [
        (pygame.image.load("subtopic buttons/algebra/expanding brackets button.jpg"), pygame.image.load("subtopic buttons/algebra/expanding brackets button.jpg").get_rect(center=(249,165)), "expbrackets_notes"),
        (pygame.image.load("subtopic buttons/algebra/factorising button.jpg"), pygame.image.load("subtopic buttons/algebra/factorising button.jpg").get_rect(center=(750,165)), "factorising_notes"),
        (pygame.image.load("subtopic buttons/algebra/inequalities button.jpg"), pygame.image.load("subtopic buttons/algebra/inequalities button.jpg").get_rect(center=(249,315)), "inequalities_notes"),
        (pygame.image.load("subtopic buttons/algebra/sequences button.jpg"), pygame.image.load("subtopic buttons/algebra/sequences button.jpg").get_rect(center=(750,315)), "sequences_notes"),
        (pygame.image.load("subtopic buttons/algebra/solving equations button.jpg"), pygame.image.load("subtopic buttons/algebra/solving equations button.jpg").get_rect(center=(249,465)), "solvingeqs_notes")
        ],

    "geometry_page": [
        (pygame.image.load("subtopic buttons/geometry/angles button.jpg"), pygame.image.load("subtopic buttons/geometry/angles button.jpg").get_rect(center=(249,165)), "angles_notes"),
        (pygame.image.load("subtopic buttons/geometry/perimeter area volume button.jpg"), pygame.image.load("subtopic buttons/geometry/perimeter area volume button.jpg").get_rect(center=(750,165)), "p/a/v_notes"),
        (pygame.image.load("subtopic buttons/geometry/pythagoras button.jpg"), pygame.image.load("subtopic buttons/geometry/pythagoras button.jpg").get_rect(center=(249,315)), "pythagoras_notes"),
        (pygame.image.load("subtopic buttons/geometry/triangles quadrilaterals button.jpg"), pygame.image.load("subtopic buttons/geometry/triangles quadrilaterals button.jpg").get_rect(center=(750,315)), "tri/quad_notes"),
        (pygame.image.load("subtopic buttons/geometry/trigonometry button.jpg"), pygame.image.load("subtopic buttons/geometry/trigonometry button.jpg").get_rect(center=(249,465)), "trigonometry_notes")
        ],

    "probability_page": [
        (pygame.image.load("subtopic buttons/probability/averages button.jpg"), pygame.image.load("subtopic buttons/probability/averages button.jpg").get_rect(center=(500,177)), "averages_notes"),
        (pygame.image.load("subtopic buttons/probability/charts graphs button.jpg"), pygame.image.load("subtopic buttons/probability/charts graphs button.jpg").get_rect(center=(500,327)), "charts_notes"),
        (pygame.image.load("subtopic buttons/probability/probability button.jpg"), pygame.image.load("subtopic buttons/probability/probability button.jpg").get_rect(center=(500,477)), "probbasics_notes")
        ],

    "ratio_page": [
        (pygame.image.load("subtopic buttons/ratio/percentages button.jpg"), pygame.image.load("subtopic buttons/ratio/percentages button.jpg").get_rect(center=(500,125)), "percentages_notes"),
        (pygame.image.load("subtopic buttons/ratio/proportions button.jpg"), pygame.image.load("subtopic buttons/ratio/proportions button.jpg").get_rect(center=(500,255)), "proportions_notes"),
        (pygame.image.load("subtopic buttons/ratio/ratios button.jpg"), pygame.image.load("subtopic buttons/ratio/ratios button.jpg").get_rect(center=(500,385)), "ratios_notes"),
        (pygame.image.load("subtopic buttons/ratio/speed distance time button.jpg"), pygame.image.load("subtopic buttons/ratio/speed distance time button.jpg").get_rect(center=(500,515)), "SDT_notes")
        ],

    "graphs_page" :[
        (pygame.image.load("subtopic buttons/graphs/coordinates button.jpg"), pygame.image.load("subtopic buttons/graphs/coordinates button.jpg").get_rect(center=(249,150)), "coordinates_notes"),
        (pygame.image.load("subtopic buttons/graphs/parallel perpendicular button.jpg"), pygame.image.load("subtopic buttons/graphs/parallel perpendicular button.jpg").get_rect(center=(750,150)), "parallelperpendicular_notes"),
        (pygame.image.load("subtopic buttons/graphs/quadratic graphs button.jpg"), pygame.image.load("subtopic buttons/graphs/quadratic graphs button.jpg").get_rect(center=(249,280)), "quadgraphs_notes"),
        (pygame.image.load("subtopic buttons/graphs/simultaneous equations button.jpg"), pygame.image.load("subtopic buttons/graphs/simultaneous equations button.jpg").get_rect(center=(750,280)), "simuleqs_notes"),
        (pygame.image.load("subtopic buttons/graphs/sin cos tan button.jpg"), pygame.image.load("subtopic buttons/graphs/sin cos tan button.jpg").get_rect(center=(249,410)), "triggraphs_notes"),
        (pygame.image.load("subtopic buttons/graphs/straight line graphs button.jpg"), pygame.image.load("subtopic buttons/graphs/straight line graphs button.jpg").get_rect(center=(750,410)), "straightline_notes"),
        (pygame.image.load("subtopic buttons/graphs/transformations button.jpg"), pygame.image.load("subtopic buttons/graphs/transformations button.jpg").get_rect(center=(500,540)), "transforming_notes")
        ]
    

    }

notes_images = {
    
    # numbers subtopic notes
    
    "typesofnumbers_notes":[
        pygame.image.load("subtopic notes/numbers/types of numbers (1).png"),
        pygame.image.load("subtopic notes/numbers/types of numbers (2).png"),
        pygame.image.load("subtopic notes/numbers/types of numbers (3).png"),
        pygame.image.load("subtopic notes/numbers/types of numbers (4).png"),
        pygame.image.load("subtopic notes/numbers/types of numbers (5).png")
        ],

    "rounding_notes":[
        pygame.image.load("subtopic notes/numbers/rounding (1).png"),
        pygame.image.load("subtopic notes/numbers/rounding (2).png"),
        pygame.image.load("subtopic notes/numbers/rounding (3).png"),
        pygame.image.load("subtopic notes/numbers/rounding (4).png"),
        pygame.image.load("subtopic notes/numbers/rounding (5).png"),
        pygame.image.load("subtopic notes/numbers/rounding (6).png")
        ],

    "placeval_notes":[
        pygame.image.load("subtopic notes/numbers/place value (1).png"),
        pygame.image.load("subtopic notes/numbers/place value (2).png"),
        ],

    "fractions_notes":[
        pygame.image.load("subtopic notes/numbers/fractions (1).png"),
        pygame.image.load("subtopic notes/numbers/fractions (2).png"),
        pygame.image.load("subtopic notes/numbers/fractions (3).png"),
        pygame.image.load("subtopic notes/numbers/fractions (4).png"),
        pygame.image.load("subtopic notes/numbers/fractions (5).png"),
        pygame.image.load("subtopic notes/numbers/fractions (6).png"),
        pygame.image.load("subtopic notes/numbers/fractions (7).png"),
        pygame.image.load("subtopic notes/numbers/fractions (8).png"),
        pygame.image.load("subtopic notes/numbers/fractions (9).png")
        ],

    "BIDMAS_notes":[
        pygame.image.load("subtopic notes/numbers/BIDMAS (1).png"),
        pygame.image.load("subtopic notes/numbers/BIDMAS (2).png"),
        pygame.image.load("subtopic notes/numbers/BIDMAS (3).png"),
        pygame.image.load("subtopic notes/numbers/BIDMAS (4).png"),
        pygame.image.load("subtopic notes/numbers/BIDMAS (5).png")
        ],
    
    "decimals_notes":[
        pygame.image.load("subtopic notes/numbers/decimals (1).png"),
        pygame.image.load("subtopic notes/numbers/decimals (2).png"),
        pygame.image.load("subtopic notes/numbers/decimals (3).png"),
        pygame.image.load("subtopic notes/numbers/decimals (4).png"),
        pygame.image.load("subtopic notes/numbers/decimals (5).png"),
        pygame.image.load("subtopic notes/numbers/decimals (6).png")
        ],

    "FDP_notes":[
        pygame.image.load("subtopic notes/numbers/FDP (1).png"),
        pygame.image.load("subtopic notes/numbers/FDP (2).png"),
        pygame.image.load("subtopic notes/numbers/FDP (3).png")
        ],

    # algebra subtopic notes
    
    "expbrackets_notes":[
        pygame.image.load("subtopic notes/algebra/expanding (1).png"),
        pygame.image.load("subtopic notes/algebra/expanding (2).png"),
        pygame.image.load("subtopic notes/algebra/expanding (3).png")
        ],
    
    "factorising_notes":[
        pygame.image.load("subtopic notes/algebra/factorising (1).png"),
        pygame.image.load("subtopic notes/algebra/factorising (2).png"),
        pygame.image.load("subtopic notes/algebra/factorising (3).png"),
        pygame.image.load("subtopic notes/algebra/factorising (4).png"),
        pygame.image.load("subtopic notes/algebra/factorising (5).png")
        ],
    
    "inequalities_notes":[
        pygame.image.load("subtopic notes/algebra/inequalities (1).png"),
        pygame.image.load("subtopic notes/algebra/inequalities (2).png"),
        pygame.image.load("subtopic notes/algebra/inequalities (3).png"),
        pygame.image.load("subtopic notes/algebra/inequalities (4).png"),
        pygame.image.load("subtopic notes/algebra/inequalities (5).png"),
        pygame.image.load("subtopic notes/algebra/inequalities (6).png"),
        pygame.image.load("subtopic notes/algebra/inequalities (7).png")
        ],
    
    "sequences_notes":[
        pygame.image.load("subtopic notes/algebra/sequences (1).png"),
        pygame.image.load("subtopic notes/algebra/sequences (2).png"),
        pygame.image.load("subtopic notes/algebra/sequences (3).png")
        ],
    
    "solvingeqs_notes":[
        pygame.image.load("subtopic notes/algebra/solving eq (1).png"),
        pygame.image.load("subtopic notes/algebra/solving eq (2).png"),
        pygame.image.load("subtopic notes/algebra/solving eq (3).png"),
        pygame.image.load("subtopic notes/algebra/solving eq (4).png"),
        pygame.image.load("subtopic notes/algebra/solving eq (5).png"),
        pygame.image.load("subtopic notes/algebra/solving eq (6).png")
        ],

    # geometry subtopic notes
    
    "angles_notes":[
        pygame.image.load("subtopic notes/geometry/angles (1).png"),
        pygame.image.load("subtopic notes/geometry/angles (2).png"),
        pygame.image.load("subtopic notes/geometry/angles (3).png"),
        pygame.image.load("subtopic notes/geometry/angles (4).png"),
        pygame.image.load("subtopic notes/geometry/angles (5).png"),
        pygame.image.load("subtopic notes/geometry/angles (6).png"),
        pygame.image.load("subtopic notes/geometry/angles (7).png")
        ],
    
    "p/a/v_notes":[
        pygame.image.load("subtopic notes/geometry/vol area (1).png"),
        pygame.image.load("subtopic notes/geometry/vol area (2).png"),
        pygame.image.load("subtopic notes/geometry/vol area (3).png"),
        pygame.image.load("subtopic notes/geometry/vol area (4).png"),
        pygame.image.load("subtopic notes/geometry/vol area (5).png"),
        pygame.image.load("subtopic notes/geometry/vol area (6).png")
        ],

    "pythagoras_notes":[
        pygame.image.load("subtopic notes/geometry/pythagoras.png")
        ],
    
    "tri/quad_notes":[
        pygame.image.load("subtopic notes/geometry/T and Q (1).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (2).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (3).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (4).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (5).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (6).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (7).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (8).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (9).png"),
        pygame.image.load("subtopic notes/geometry/T and Q (10).png")
        ],
    
    "trigonometry_notes":[
        pygame.image.load("subtopic notes/geometry/TRIG (1).png"),
        pygame.image.load("subtopic notes/geometry/TRIG (2).png"),
        pygame.image.load("subtopic notes/geometry/TRIG (3).png"),
        pygame.image.load("subtopic notes/geometry/TRIG (4).png"),
        pygame.image.load("subtopic notes/geometry/TRIG (5).png")
        ],
        
    # probability subtopic notes
    
    "averages_notes":[
        pygame.image.load("subtopic notes/probability/avgs (1).png"),
        pygame.image.load("subtopic notes/probability/avgs (2).png")
        ],
    
    "charts_notes":[
        pygame.image.load("subtopic notes/probability/charts graphs (1).png"),
        pygame.image.load("subtopic notes/probability/charts graphs (2).png"),
        pygame.image.load("subtopic notes/probability/charts graphs (3).png"),
        pygame.image.load("subtopic notes/probability/charts graphs (4).png"),
        pygame.image.load("subtopic notes/probability/charts graphs (5).png")
        ],
    
    "probbasics_notes":[
        pygame.image.load("subtopic notes/probability/prob basics.png")
        ],

    # ratio subtopic notes
    
    "percentages_notes":[
        pygame.image.load("subtopic notes/ratio/percentages (1).png"),
        pygame.image.load("subtopic notes/ratio/percentages (2).png")
        ],
    
    "proportions_notes":[
        pygame.image.load("subtopic notes/ratio/prop (1).png"),
        pygame.image.load("subtopic notes/ratio/prop (2).png"),
        pygame.image.load("subtopic notes/ratio/prop (3).png"),
        pygame.image.load("subtopic notes/ratio/prop (4).png")
        ],
    
    "ratios_notes":[
        pygame.image.load("subtopic notes/ratio/ratios (1).png"),
        pygame.image.load("subtopic notes/ratio/ratios (2).png"),
        pygame.image.load("subtopic notes/ratio/ratios (3).png"),
        pygame.image.load("subtopic notes/ratio/ratios (4).png")
        ],
    
    "SDT_notes":[
        pygame.image.load("subtopic notes/ratio/SDT.png")
        ],

    # graphs subtopic notes
    
    "coordinates_notes":[
        pygame.image.load("subtopic notes/graphs/coordinates.png")
        ],
    
    "parallelperpendicular_notes":[
        pygame.image.load("subtopic notes/graphs/parallel perpendicular (1).png"),
        pygame.image.load("subtopic notes/graphs/parallel perpendicular (2).png"),
        pygame.image.load("subtopic notes/graphs/parallel perpendicular (3).png"),
        pygame.image.load("subtopic notes/graphs/parallel perpendicular (4).png")
        ],
    
    "quadgraphs_notes":[
        pygame.image.load("subtopic notes/graphs/quadratic (1).png"),
        pygame.image.load("subtopic notes/graphs/quadratic (2).png"),
        pygame.image.load("subtopic notes/graphs/quadratic (3).png"),
        pygame.image.load("subtopic notes/graphs/quadratic (4).png"),
        pygame.image.load("subtopic notes/graphs/quadratic (5).png"),
        pygame.image.load("subtopic notes/graphs/quadratic (6).png")
        ],
    
    "simuleqs_notes":[
        pygame.image.load("subtopic notes/graphs/simul (1).png"),
        pygame.image.load("subtopic notes/graphs/simul (2).png"),
        pygame.image.load("subtopic notes/graphs/simul (3).png")
        ],
    
    "triggraphs_notes":[
        pygame.image.load("subtopic notes/graphs/sin cos tan (1).png"),
        pygame.image.load("subtopic notes/graphs/sin cos tan (2).png"),
        pygame.image.load("subtopic notes/graphs/sin cos tan (3).png"),
        pygame.image.load("subtopic notes/graphs/sin cos tan (4).png")
        ],
    
    "straightline_notes":[
        pygame.image.load("subtopic notes/graphs/straight lines (1).png"),
        pygame.image.load("subtopic notes/graphs/straight lines (2).jpg"),
        pygame.image.load("subtopic notes/graphs/straight lines (3).png"),
        pygame.image.load("subtopic notes/graphs/straight lines (4).png"),
        pygame.image.load("subtopic notes/graphs/straight lines (5).png"),
        pygame.image.load("subtopic notes/graphs/straight lines (6).png"),
        pygame.image.load("subtopic notes/graphs/straight lines (7).png")
        ],
    
    "transforming_notes":[
        pygame.image.load("subtopic notes/graphs/transforming (1).png"),
        pygame.image.load("subtopic notes/graphs/transforming (2).png"),
        pygame.image.load("subtopic notes/graphs/transforming (3).png"),
        pygame.image.load("subtopic notes/graphs/transforming (4).png"),
        pygame.image.load("subtopic notes/graphs/transforming (5).png"),
        pygame.image.load("subtopic notes/graphs/transforming (6).png"),
        pygame.image.load("subtopic notes/graphs/transforming (7).png"),
        pygame.image.load("subtopic notes/graphs/transforming (8).png"),
        pygame.image.load("subtopic notes/graphs/transforming (9).png")
        ]
        
    }

current_notes_page = {topic: 0 for topic in notes_images}


pygame.display.flip()

PreviousPage = None

# main game loop

running = True
while running:
    
    score_text = font.render(str(score), True, WHITE)

    q_data = questions[current_question]
    
    mouse_position = pygame.mouse.get_pos()


    if CurrentPage == MainMenu:
        attempts = 0
        score = 0
        current_question = 0
        random.shuffle(questions)
        q_data = questions[current_question]
        shuffle_answers(questions[current_question])
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if CurrentPage == MainMenu:
                if rev_button.collidepoint(mouse_position):
                    PreviousPage = CurrentPage
                    CurrentPage = RevisionNotes_Page
                    pygame.event.clear()
                    break
                
                if game_button.collidepoint(mouse_position):
                    attempts = 0
                    PreviousPage = CurrentPage
                    CurrentPage = GamePage
                    pygame.event.clear()
                    break



            elif CurrentPage == GamePage:
                x,y = event.pos
                for i, pos in enumerate(positions):
                    if pygame.Rect(pos, (405, 82)).collidepoint(x, y):
                        selected_ans = i
                        if selected_ans == q_data["correct"]:
                            score = score + 1
                            pygame.time.delay(50)
                            current_question = (current_question + 1) % len(questions)
                            shuffle_answers(questions[current_question])
                            pygame.event.clear()
                            selected_ans = None
                        else:
                            attempts = attempts + 1
                            
                            if attempts == 1:
                                HB_IMG = HB_2
                                print("Wrong, try again!")

                            elif attempts == 2:
                                HB_IMG = HB_1
                                print("Wrong, try again!")
                            
                            
                            elif attempts >= 3:
                                CurrentPage = GameOverPage
                                pygame.event.clear()
                                break
                            
                            else:
                                print("Wrong! Try again.")
                                pygame.event.clear()
                        break

                pygame.event.pump()
                
                    
         
            elif CurrentPage == GameOverPage:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if retry_button.collidepoint(event.pos):
                        CurrentPage = GamePage
                        attempts = 0
                        score = 0
                        current_question = 0
                        random.shuffle(questions)
                        q_data = questions[current_question]
                        shuffle_answers(questions[current_question])
                        pygame.event.clear()
                    elif M_menu_button.collidepoint(event.pos):
                        CurrentPage = MainMenu
                        pygame.event.clear()
                        
                

                
            elif CurrentPage == RevisionNotes_Page:
                for KS4_button_img, rect, KS4_topic_page in KS4_buttons:
                    if rect.collidepoint(mouse_position):
                        PreviousPage = CurrentPage
                        CurrentPage = KS4_topic_page
                if back_button.collidepoint(mouse_position):
                    CurrentPage = MainMenu



            elif CurrentPage in KS4_subtopic_buttons:
                for button_img, rect, subtopic_page in KS4_subtopic_buttons[CurrentPage]:
                    if rect.collidepoint(mouse_position):
                        PreviousPage = CurrentPage
                        CurrentPage = subtopic_page
                        current_notes_page[CurrentPage] = 0
                    if back_button.collidepoint(mouse_position):
                        CurrentPage = RevisionNotes_Page



            elif CurrentPage in notes_images:
                if CurrentPage in current_notes_page:
                    
                    if topic_pg_back_button.collidepoint(mouse_position):
                        CurrentPage = RevisionNotes_Page
                        
                    if next_button.collidepoint(mouse_position):
                        if current_notes_page[CurrentPage] < len(notes_images[CurrentPage]) - 1:
                            current_notes_page[CurrentPage]+= 1
                    if previous_button.collidepoint(mouse_position):
                        if current_notes_page[CurrentPage] > 0:
                            current_notes_page[CurrentPage] -= 1
            



            elif CurrentPage in KS4_topics_pages:
                if back_button.collidepoint(mouse_position):
                    CurrentPage = PreviousPage
            elif topic_pg_back_button.collidepoint(mouse_position):
                CurrentPage = RevisionNotes_Page

                        

# conditional (IF/ ELIF) statements (mainly for blitting each page)


    if CurrentPage == MainMenu:
        screen.fill(WHITE)
        screen.blit(main_menu_writing, (0,-25))
        screen.blit(game_button_image, game_button)
        screen.blit(rev_button_image, rev_button)

    # game page

    if CurrentPage == GamePage:
        screen.fill(WHITE)
        screen.blit(q_data["questionIMG"], (0, 0))
        screen.blit(HB_IMG, (0, 0))
        
        
        positions = [(94, 530), (507, 530), (94, 425), (507,425)]
        for i, pos in enumerate(positions):
            screen.blit(q_data["answersIMG"][i],pos)
            


    # game over page

    if CurrentPage == GameOverPage:
        HB_IMG = HB_3
        screen.blit(game_over_page, (0, 0))
        screen.blit(retry_button_image, retry_button)
        screen.blit(M_menu_button_image, M_menu_button)

        
        screen.blit(score_text, (614,482))
        screen.blit(scorewriting, (320, 482))
        


    # revision notes section        
    
    elif CurrentPage == RevisionNotes_Page:
        screen.fill(WHITE)
        screen.blit(KS4_rev_notes_title,(0,-15))
        screen.blit(back_button_image, back_button)
        for KS4_button_img, rect, KS4_topic_page in KS4_buttons:
            screen.blit(KS4_button_img, rect)
        pygame.display.flip()

    elif CurrentPage in KS4_topics_pages:
        screen.blit(KS4_topics_pages[CurrentPage], (0, 0))
        screen.blit(back_button_image, back_button)
        for button_img, rect, subtopic_page in KS4_subtopic_buttons.get(CurrentPage, []):
            screen.blit(button_img, rect) 

    elif CurrentPage in notes_images:
        screen.blit(notes_images[CurrentPage][current_notes_page[CurrentPage]], (0,0))
        screen.blit(topic_pg_back_button_IMG, topic_pg_back_button)

        if CurrentPage in current_notes_page:
            if current_notes_page[CurrentPage] < len(notes_images[CurrentPage])-1:
                screen.blit(right_button_IMG, next_button)

            if current_notes_page[CurrentPage] > 0:
                screen.blit(left_button_IMG, previous_button)


    pygame.display.flip()

pygame.display.flip()

pygame.quit()
